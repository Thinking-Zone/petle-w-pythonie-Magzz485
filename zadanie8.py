pada = False  # Zmienna kontrolująca pętlę
licznik_nie = 0  # Zmienna licząca odpowiedzi "nie"

while not pada:
    odpowiedz = input("Czy pada? (tak/nie): ").lower()  # Pobieramy odpowiedź użytkownika i zamieniamy na małe litery
    
    if odpowiedz == "tak":
        print(f"Program zakończony. Odpowiedziałeś 'nie' {licznik_nie} razy.")
        break  # Zakończenie programu, gdy użytkownik odpowie "tak"
    
    elif odpowiedz == "nie":
        licznik_nie += 1  # Zwiększamy licznik, gdy odpowiedź to "nie"
    
    elif odpowiedz == "nie wiem
