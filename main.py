import os
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai
from produse import produse

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

catalog_text = ""
for produs in produse:
    catalog_text += f"- Cod: {produs['cod']}, Nume: {produs['nume']}, Preț: {produs['pret']} USD, Stoc: {produs['stoc']}, Categorie: {produs['categorie']}\n"

system_prompt = f"""Ești asistentul virtual al magazinului MobilaPlus & Construct.
Vindem atât materiale de construcție, cât și mobilă.

Ai acces la următorul catalog de produse:
{catalog_text}

Reguli generale:
- Răspunde doar despre produsele din catalog
- Când recomanzi un produs, menționează codul (ex: MC-001 sau MB-001)
- Dacă un produs nu e în stoc, spune clar și oferă o alternativă din aceeași categorie
- Fii prietenos și concis
- Răspunde întotdeauna în aceeași limbă în care utilizatorul a scris mesajul

Reguli speciale pentru PROIECTE (când clientul descrie o lucrare, nu un produs specific):
Dacă cineva spune ceva de genul "vreau să-mi fac acoperișul", "vreau să pun gresie în curte",
"vreau să-mi renovez baia", "vreau să izolez casa" — NU căuta un singur produs.
În schimb, gândește-te ca un specialist în construcții și recomandă o LISTĂ completă de
materiale necesare pentru acel proiect, cu codurile corespunzătoare din catalog.

Exemple de raționament (ghidează-te după acest tip de logică pentru orice proiect menționat):
- Acoperiș nou: tigla/tabla, șipci lemn, membrană anticondens, jgheaburi, burlane, coamă, parazăpezi
- Gresie curte/terasă: gresie exterior antiderapantă, mortar adeziv, chit rosturi, profile finisaj
- Renovare baie: gresie, faianță, vas WC, lavoar, baterie, cadă, silicon sanitar, sifon
- Izolare casă: vată minerală sau polistiren, folie vapori, bandă etanșare, spumă poliuretanică
- Zid nou: cărămidă sau BCA, mortar/ciment, var
- Vopsit interior: grund universal, vopsea lavabilă, bandă mascare, diluant

Pentru orice proiect, întreabă suprafața aproximativă (mp) dacă lipsește, ca să poți estima
cantități, apoi oferă o listă clară cu produse, cantități estimate și cost total aproximativ.
Dacă un material nu e în stoc, propune imediat alternativa disponibilă.
"""

model = genai.GenerativeModel("gemini-flash-latest", system_instruction=system_prompt)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    mesaj_utilizator = request.json.get("message")
    raspuns = model.generate_content(mesaj_utilizator)
    return jsonify({"reply": raspuns.text})


if __name__ == "__main__":
    app.run(debug=True)