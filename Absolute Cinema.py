# STAP 1: Vraag de naam van de bezoeker.
naam = input("Wat is je naam? ").strip().title()

# STAP 2: Vraag naar de leeftijd van de gebruiker en cast deze naar het juiste datatype.
leeftijd = int(input("Wat is je leeftijd? "))

# STAP 3: Vraag naar de film die de bezoeker wilt zien
film_input = input("Welke film wil je zien? ").strip().title()

# STAP 4: Lijst met beschikbare films (pas deze aan naar je eigen favorieten!)
films = ["Demon Slayer", "Fastastic four", "The conjuring", "Superman (2025)", "How to train your dragon", "Weapons"]


if film_input not in films:
    print(f"Sorry, deze '{film_input}' draait (nu) niet in deze bioscoop.")
    exit()  

# STAP 5: Vraag hoeveel kaartjes de gebruiker wilt bestellen en cast deze naar het juiste datatype
aantal_kaartjes = int(input("Hoeveel kaartjes wil je bestellen? "))

# STAP 6: Bepaal het tarief en de prijs per kaartje op basis van leeftijd
if leeftijd < 3:
    prijs_per_kaartje = 0.00
    tarief = "Gratis"
elif 3 <= leeftijd <= 12:
    prijs_per_kaartje = 7.00
    tarief = "Kinder tarief"
elif 13 <= leeftijd <= 64:
    prijs_per_kaartje = 12.00
    tarief = "Standaard tarief"
else:  # leeftijd >= 65
    prijs_per_kaartje = 9.00
    tarief = "65+ tarief"

# stap 7 Vraag of gebruiker popcorn wil
popcorn_input = input("Wil je popcorn bestellen voor €5,70 per kaartje? (j/ja/n/nee): ").strip().lower()
if popcorn_input in ["j", "ja"]:
    popcorn_besteld = True
    popcorn_prijs = 5.70 * aantal_kaartjes
else:
    popcorn_besteld = False
    popcorn_prijs = 0

# STAP 10: Bereken totaalprijs
totaalprijs = (prijs_per_kaartje * aantal_kaartjes) + popcorn_prijs

# STAP 11 Print overzicht
print("\n--- Kassabon ---")
print(f"Klant: {naam}")
print(f"Film: {film_input}")
print(f"Leeftijd: {leeftijd} jaar - {tarief}")
print(f"Aantal kaartjes: {aantal_kaartjes}")s
print(f"Prijs per kaartje: €{prijs_per_kaartje:.2f}")
if popcorn_besteld:
    print(f"Popcorn: Ja (+€{5.70:.2f} per kaartje)")
else:
    print("Popcorn: Nee")
print(f"Totaalprijs: €{totaalprijs:.2f}")
print("----------------")
