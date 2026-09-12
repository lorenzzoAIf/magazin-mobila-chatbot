# Materiale de construcție, organizate pe categorii
# Fiecare categorie: (nume produs, preț MDL, stoc)
categorii_materiale = {
    "Ciment si mortar": [
        ("Ciment Portland M400 25kg", 7, 150),
        ("Ciment Portland M500 25kg", 8, 120),
        ("Mortar adeziv gresie 25kg", 6, 90),
        ("Mortar reparatii beton 25kg", 9, 60),
        ("Var hidratat 25kg", 4, 80),
    ],
    "Caramida si BCA": [
        ("Caramida plina 25x12x6cm", 0.4, 5000),
        ("BCA 60x25x20cm", 2, 800),
        ("BCA 60x25x25cm", 3, 700),
        ("Caramida GVP 25x25x14cm", 2, 1200),
        ("Bolt ceramic 25x19x19cm", 2, 900),
    ],
    "Cherestea": [
        ("Grinda lemn 10x10cm 3m", 11, 200),
        ("Sipca lemn 3x5cm 4m", 2, 400),
        ("Placaj 18mm 250x125cm", 36, 100),
        ("OSB 18mm 250x125cm", 30, 120),
        ("Rigla lemn brad 5x8cm 4m", 5, 300),
        ("Lambriu lemn 12mm mp", 9, 250),
        ("Dulap lemn brad 5x15cm 4m", 12, 150),
        ("Grinda lemn 15x15cm 4m", 19, 100),
    ],
    "Gresie si faianta": [
        ("Gresie interior 60x60cm mp", 9, 500),
        ("Gresie exterior antiderapanta mp", 11, 300),
        ("Faianta baie 30x60cm mp", 8, 400),
        ("Gresie portelanata 80x80cm mp", 15, 250),
        ("Mozaic decorativ mp", 18, 100),
        ("Gresie terasa 40x40cm mp", 7, 350),
        ("Faianta bucatarie 25x40cm mp", 8, 300),
        ("Gresie rectificata 60x120cm mp", 17, 150),
        ("Plinta ceramica ml", 3, 500),
        ("Profil finisaj gresie ml", 2, 400),
    ],
    "Vopsele": [
        ("Vopsea lavabila alba 15L", 24, 200),
        ("Vopsea lavabila colorata 10L", 28, 150),
        ("Grund universal 10L", 17, 180),
        ("Vopsea exterior fatade 15L", 32, 100),
        ("Vopsea email metal 2.5L", 13, 120),
        ("Vopsea rezistenta umezeala 10L", 26, 90),
        ("Lac parchet 2.5L", 14, 100),
        ("Vopsea termorezistenta 1L", 9, 80),
        ("Diluant universal 5L", 6, 150),
        ("Amorsa aderenta 5L", 11, 130),
    ],
    "Izolatii": [
        ("Vata minerala 10cm mp", 5, 300),
        ("Polistiren expandat 10cm mp", 4, 400),
        ("Polistiren extrudat 5cm mp", 7, 250),
        ("Membrana hidroizolatoare 10mp rola", 36, 80),
        ("Folie vapori 50mp rola", 18, 100),
        ("Vata bazaltica 5cm mp", 6, 200),
        ("Spuma poliuretanica 750ml", 5, 300),
        ("Banda etansare ferestre ml", 2, 400),
    ],
    "Instalatii sanitare": [
        ("Teava PPR 20mm ml", 1, 1000),
        ("Teava PPR 25mm ml", 2, 800),
        ("Robinet baterie bucatarie", 44, 60),
        ("Baterie dus", 49, 50),
        ("Vas WC complet", 91, 40),
        ("Lavoar ceramica", 55, 45),
        ("Cada baie 170cm", 129, 20),
        ("Sifon pardoseala", 7, 200),
        ("Reductie PPR 20-25mm", 1, 500),
        ("Cot PPR 90 grade", 1, 600),
    ],
    "Instalatii electrice": [
        ("Cablu electric 2.5mm ml", 1, 2000),
        ("Cablu electric 1.5mm ml", 1, 2500),
        ("Priza simpla", 2, 300),
        ("Intrerupator simplu", 3, 300),
        ("Tablou electric 12 module", 36, 50),
        ("Siguranta automata 16A", 5, 150),
        ("Doza derivatie", 1, 400),
        ("Corp iluminat LED patrat", 19, 100),
        ("Bec LED 9W", 2, 500),
        ("Tub protectie cablu ml", 1, 800),
    ],
    "Usi si ferestre": [
        ("Usa interior lemn 80cm", 91, 40),
        ("Usa exterior metalica", 242, 20),
        ("Fereastra PVC 120x140cm", 170, 30),
        ("Fereastra PVC 100x120cm", 132, 35),
        ("Toc usa interior", 24, 50),
        ("Clanta usa inox", 9, 100),
        ("Balama usa", 3, 200),
        ("Plasa insecte fereastra", 16, 60),
    ],
    "Acoperis": [
        ("Tigla ceramica buc", 1, 3000),
        ("Tabla cutata mp", 9, 400),
        ("Jgheab PVC ml", 7, 200),
        ("Burlan PVC ml", 6, 200),
        ("Membrana anticondens 75mp rola", 44, 60),
        ("Sipca lemn acoperis ml", 2, 500),
        ("Coama tigla ml", 5, 150),
        ("Parazapada buc", 8, 100),
    ],
    "Scule si accesorii": [
        ("Bormasina electrica", 71, 40),
        ("Flex unghiular", 57, 35),
        ("Nivela laser", 44, 30),
        ("Ciocan 500g", 7, 100),
        ("Surubelnita set", 12, 80),
        ("Metru rulant 5m", 5, 150),
        ("Manusi protectie", 3, 300),
        ("Ochelari protectie", 4, 200),
        ("Scara aluminiu 3m", 77, 25),
        ("Pistol silicon", 9, 90),
    ],
    "Adezivi si chit": [
        ("Silicon sanitar 300ml", 4, 300),
        ("Chit rosturi gresie 5kg", 7, 200),
        ("Adeziv PVC 500ml", 4, 150),
        ("Spuma montaj usi 750ml", 6, 180),
        ("Chit lemn 500g", 5, 120),
        ("Adeziv gresie exterior 25kg", 9, 100),
        ("Banda mascare 50m", 2, 250),
        ("Chit reparatii fisuri 1kg", 6, 90),
    ],
}

categorii_mobila = {
    "Canapele": [
        ("Canapea 3 locuri Oslo", 505, 5),
        ("Canapea colt Gothenburg", 648, 2),
        ("Canapea extensibila Bergen", 566, 4),
    ],
    "Mese": [
        ("Masa dining Stockholm", 242, 8),
        ("Masa cafea Copenhaga", 77, 15),
        ("Masa laterala Jonkoping", 59, 18),
        ("Masa birou Orebro", 181, 9),
    ],
    "Dulapuri": [
        ("Dulap dormitor Bergen", 363, 3),
        ("Dulap living Uppsala", 484, 0),
        ("Comoda TV Aarhus", 151, 6),
        ("Biblioteca Linkoping", 272, 3),
    ],
    "Scaune": [
        ("Scaun birou Helsinki", 91, 12),
        ("Scaun sufragerie Lund", 45, 20),
        ("Fotoliu relaxare Helsingborg", 332, 4),
    ],
    "Paturi": [
        ("Pat matrimonial Malmo", 423, 4),
        ("Pat single Vasteras", 220, 7),
        ("Saltea memory 160x200", 283, 10),
    ],
    "Bucatarie": [
        ("Set mobilier bucatarie 3m", 907, 3),
        ("Masa bucatarie extensibila", 192, 6),
        ("Scaun bar bucatarie", 65, 15),
    ],
    "Diverse": [
        ("Oglinda perete decorativa", 70, 10),
        ("Covor living 200x300", 137, 8),
    ],
}

produse = []
contor = 1
for categorie, items in categorii_materiale.items():
    for nume, pret, stoc in items:
        cod = f"MC-{contor:03d}"
        produse.append({
            "cod": cod,
            "nume": nume,
            "pret": pret,
            "stoc": stoc,
            "categorie": categorie,
            "tip": "material"
        })
        contor += 1

contor = 1
for categorie, items in categorii_mobila.items():
    for nume, pret, stoc in items:
        cod = f"MB-{contor:03d}"
        produse.append({
            "cod": cod,
            "nume": nume,
            "pret": pret,
            "stoc": stoc,
            "categorie": categorie,
            "tip": "mobila"
        })
        contor += 1


def cauta_produs(cod):
    for produs in produse:
        if produs["cod"] == cod:
            return produs
    return None


def filtreaza_categorie(categorie):
    return [p for p in produse if p["categorie"].lower() == categorie.lower()]


def verifica_stoc(cod):
    produs = cauta_produs(cod)
    if produs is None:
        return "Produs inexistent"
    if produs["stoc"] > 0:
        return f"În stoc: {produs['stoc']} bucăți"
    return "Stoc epuizat"