import random

# Losowanie, czy pada deszcz, czy nie
pogoda = random.choice(["pada", "nie pada"])

# Pętla, która pyta użytkownika o pogodę, dopóki nie zgadnie
while True:
    odpowiedz = input("Czy pada deszcz? (pada/nie pada): ").lower()  # Pobranie odpowiedzi i zamiana na małe litery
    if odpowiedz == pogoda:
        print("Brawo! Zgadłeś!")
        break  # Przerwanie pętli, jeśli odpowiedź była poprawna
    else:
        print("Niestety, spróbuj ponownie.")
