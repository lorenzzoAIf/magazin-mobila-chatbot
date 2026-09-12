# Materiale de construcție, organizate pe categorii
# Fiecare categorie: (nume produs, preț MDL, stoc)
categorii_materiale = {
    "Ciment si mortar": [
        ("Ciment Portland M400 25kg", 120, 150),
        ("Ciment Portland M500 25kg", 140, 120),
        ("Mortar adeziv gresie 25kg", 105, 90),
        ("Mortar reparatii beton 25kg", 165, 60),
        ("Var hidratat 25kg", 80, 80),
    ],
    "Caramida si BCA": [
        ("Caramida plina 25x12x6cm", 8, 5000),
        ("BCA 60x25x20cm", 45, 800),
        ("BCA 60x25x25cm", 55, 700),
        ("Caramida GVP 25x25x14cm", 30, 1200),
        ("Bolt ceramic 25x19x19cm", 33, 900),
    ],
    "Cherestea": [
        ("Grinda lemn 10x10cm 3m", 200, 200),
        ("Sipca lemn 3x5cm 4m", 45, 400),
        ("Placaj 18mm 250x125cm", 650, 100),
        ("OSB 18mm 250x125cm", 550, 120),
        ("Rigla lemn brad 5x8cm 4m", 90, 300),
        ("Lambriu lemn 12mm mp", 165, 250),
        ("Dulap lemn brad 5x15cm 4m", 220, 150),
        ("Grinda lemn 15x15cm 4m", 350, 100),
    ],
    "Gresie si faianta": [
        ("Gresie interior 60x60cm mp", 165, 500),
        ("Gresie exterior antiderapanta mp", 200, 300),
        ("Faianta baie 30x60cm mp", 145, 400),
        ("Gresie portelanata 80x80cm mp", 270, 250),
        ("Mozaic decorativ mp", 330, 100),
        ("Gresie terasa 40x40cm mp", 130, 350),
        ("Faianta bucatarie 25x40cm mp", 140, 300),
        ("Gresie rectificata 60x120cm mp", 310, 150),
        ("Plinta ceramica ml", 55, 500),
        ("Profil finisaj gresie ml", 45, 400),
    ],
    "Vopsele": [
        ("Vopsea lavabila alba 15L", 440, 200),
        ("Vopsea lavabila colorata 10L", 510, 150),
        ("Grund universal 10L", 310, 180),
        ("Vopsea exterior fatade 15L", 580, 100),
        ("Vopsea email metal 2.5L", 235, 120),
        ("Vopsea rezistenta umezeala 10L", 470, 90),
        ("Lac parchet 2.5L", 255, 100),
        ("Vopsea termorezistenta 1L", 165, 80),
        ("Diluant universal 5L", 110, 150),
        ("Amorsa aderenta 5L", 200, 130),
    ],
    "Izolatii": [
        ("Vata minerala 10cm mp", 90, 300),
        ("Polistiren expandat 10cm mp", 75, 400),
        ("Polistiren extrudat 5cm mp", 130, 250),
        ("Membrana hidroizolatoare 10mp rola", 650, 80),
        ("Folie vapori 50mp rola", 330, 100),
        ("Vata bazaltica 5cm mp", 110, 200),
        ("Spuma poliuretanica 750ml", 90, 300),
        ("Banda etansare ferestre ml", 30, 400),
    ],
    "Instalatii sanitare": [
        ("Teava PPR 20mm ml", 22, 1000),
        ("Teava PPR 25mm ml", 30, 800),
        ("Robinet baterie bucatarie", 800, 60),
        ("Baterie dus", 900, 50),
        ("Vas WC complet", 1650, 40),
        ("Lavoar ceramica", 1000, 45),
        ("Cada baie 170cm", 2350, 20),
        ("Sifon pardoseala", 125, 200),
        ("Reductie PPR 20-25mm", 18, 500),
        ("Cot PPR 90 grade", 15, 600),
    ],
    "Instalatii electrice": [
        ("Cablu electric 2.5mm ml", 15, 2000),
        ("Cablu electric 1.5mm ml", 11, 2500),
        ("Priza simpla", 45, 300),
        ("Intrerupator simplu", 55, 300),
        ("Tablou electric 12 module", 650, 50),
        ("Siguranta automata 16A", 90, 150),
        ("Doza derivatie", 18, 400),
        ("Corp iluminat LED patrat", 345, 100),
        ("Bec LED 9W", 30, 500),
        ("Tub protectie cablu ml", 11, 800),
    ],
    "Usi si ferestre": [
        ("Usa interior lemn 80cm", 1650, 40),
        ("Usa exterior metalica", 4400, 20),
        ("Fereastra PVC 120x140cm", 3100, 30),
        ("Fereastra PVC 100x120cm", 2400, 35),
        ("Toc usa interior", 440, 50),
        ("Clanta usa inox", 165, 100),
        ("Balama usa", 55, 200),
        ("Plasa insecte fereastra", 290, 60),
    ],
    "Acoperis": [
        ("Tigla ceramica buc", 18, 3000),
        ("Tabla cutata mp", 165, 400),
        ("Jgheab PVC ml", 130, 200),
        ("Burlan PVC ml", 110, 200),
        ("Membrana anticondens 75mp rola", 800, 60),
        ("Sipca lemn acoperis ml", 30, 500),
        ("Coama tigla ml", 90, 150),
        ("Parazapada buc", 145, 100),
    ],
    "Scule si accesorii": [
        ("Bormasina electrica", 1300, 40),
        ("Flex unghiular", 1030, 35),
        ("Nivela laser", 800, 30),
        ("Ciocan 500g", 130, 100),
        ("Surubelnita set", 220, 80),
        ("Metru rulant 5m", 90, 150),
        ("Manusi protectie", 55, 300),
        ("Ochelari protectie", 75, 200),
        ("Scara aluminiu 3m", 1400, 25),
        ("Pistol silicon", 165, 90),
    ],
    "Adezivi si chit": [
        ("Silicon sanitar 300ml", 65, 300),
        ("Chit rosturi gresie 5kg", 130, 200),
        ("Adeziv PVC 500ml", 80, 150),
        ("Spuma montaj usi 750ml", 105, 180),
        ("Chit lemn 500g", 90, 120),
        ("Adeziv gresie exterior 25kg", 155, 100),
        ("Banda mascare 50m", 45, 250),
        ("Chit reparatii fisuri 1kg", 110, 90),
    ],
}

categorii_mobila = {
    "Canapele": [
        ("Canapea 3 locuri Oslo", 9200, 5),
        ("Canapea colt Gothenburg", 11800, 2),
        ("Canapea extensibila Bergen", 10300, 4),
    ],
    "Mese": [
        ("Masa dining Stockholm", 4400, 8),
        ("Masa cafea Copenhaga", 1400, 15),
        ("Masa laterala Jonkoping", 1070, 18),
        ("Masa birou Orebro", 3300, 9),
    ],
    "Dulapuri": [
        ("Dulap dormitor Bergen", 6600, 3),
        ("Dulap living Uppsala", 8800, 0),
        ("Comoda TV Aarhus", 2750, 6),
        ("Biblioteca Linkoping", 4950, 3),
    ],
    "Scaune": [
        ("Scaun birou Helsinki", 1650, 12),
        ("Scaun sufragerie Lund", 810, 20),
        ("Fotoliu relaxare Helsingborg", 6050, 4),
    ],
    "Paturi": [
        ("Pat matrimonial Malmo", 7700, 4),
        ("Pat single Vasteras", 4000, 7),
        ("Saltea memory 160x200", 5150, 10),
    ],
    "Bucatarie": [
        ("Set mobilier bucatarie 3m", 16500, 3),
        ("Masa bucatarie extensibila", 3500, 6),
        ("Scaun bar bucatarie", 1180, 15),
    ],
    "Diverse": [
        ("Oglinda perete decorativa", 1280, 10),
        ("Covor living 200x300", 2500, 8),
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