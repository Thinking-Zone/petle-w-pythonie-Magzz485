# Zadanie:
# Napisz program, który obliczy sumę liczb, które są jednocześnie podzielne przez 3 i 5 w zakresie od 1 do 1000 (włącznie).
# Program powinien wypisać wynik sumy.

# Rozwiązanie w Pythonie:

suma = 0  # Zmienna do przechowywania sumy

# Pętla przechodząca przez liczby od 1 do 1000
for i in range(1, 1001):
    if i % 3 == 0 and i % 5 == 0:  # Sprawdzamy, czy liczba jest podzielna zarówno przez 3, jak i przez 5
        suma += i  # Dodajemy liczbę do sumy

# Wypisujemy wynik
print("Suma liczb podzielnych przez 3 i 5 w zakresie od 1 do 1000 wynosi:", suma)
