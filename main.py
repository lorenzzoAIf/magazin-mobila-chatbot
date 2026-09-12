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
    catalog_text += f"- Cod: {produs['cod']}, Nume: {produs['nume']}, Preț: {produs['pret']} RON, Stoc: {produs['stoc']}\n"

system_prompt = f"""Ești asistentul virtual al magazinului MobilaPlus.
Ai acces la următorul catalog de produse:
{catalog_text}
Reguli:
- Răspunde doar despre produsele din catalog
- Când recomanzi un produs, menționează codul (ex: MB-001)
- Dacă un produs nu e în stoc, spune clar
- Fii prietenos și concis
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