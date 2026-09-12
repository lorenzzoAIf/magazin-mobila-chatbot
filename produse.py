produse = [
    {"cod": "MB-001", "nume": "Canapea 3 locuri Oslo", "pret": 2500, "stoc": 5, "categorie": "Canapele"},
    {"cod": "MB-002", "nume": "Masă dining Stockholm", "pret": 1200, "stoc": 8, "categorie": "Mese"},
    {"cod": "MB-003", "nume": "Dulap dormitor Bergen", "pret": 1800, "stoc": 3, "categorie": "Dulapuri"},
    {"cod": "MB-004", "nume": "Scaun birou Helsinki", "pret": 450, "stoc": 12, "categorie": "Scaune"},
    {"cod": "MB-005", "nume": "Pat matrimonial Malmo", "pret": 2100, "stoc": 4, "categorie": "Paturi"},
    {"cod": "MB-006", "nume": "Canapea colț Gothenburg", "pret": 3200, "stoc": 2, "categorie": "Canapele"},
    {"cod": "MB-007", "nume": "Masă cafea Copenhaga", "pret": 380, "stoc": 15, "categorie": "Mese"},
    {"cod": "MB-008", "nume": "Comodă TV Aarhus", "pret": 750, "stoc": 6, "categorie": "Comode"},
    {"cod": "MB-009", "nume": "Scaun sufragerie Lund", "pret": 220, "stoc": 20, "categorie": "Scaune"},
    {"cod": "MB-010", "nume": "Dulap living Uppsala", "pret": 2400, "stoc": 0, "categorie": "Dulapuri"},
    {"cod": "MB-011", "nume": "Pat single Vasteras", "pret": 1100, "stoc": 7, "categorie": "Paturi"},
    {"cod": "MB-012", "nume": "Birou lucru Orebro", "pret": 890, "stoc": 9, "categorie": "Birouri"},
    {"cod": "MB-013", "nume": "Bibliotecă Linkoping", "pret": 1350, "stoc": 3, "categorie": "Rafturi"},
    {"cod": "MB-014", "nume": "Fotoliu relaxare Helsingborg", "pret": 1650, "stoc": 4, "categorie": "Fotolii"},
    {"cod": "MB-015", "nume": "Măsuță laterală Jonkoping", "pret": 290, "stoc": 18, "categorie": "Mese"},
]

for produs in produse:
    print(f"{produs['cod']} {produs['nume']} {produs['pret']} RON")

def cauta_produs(cod):
    for produs in produse:
        if produs["cod"] == cod:
            return produs
    return None
rezultat = cauta_produs("MB-002")
print(rezultat)
