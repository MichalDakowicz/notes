def horner(liczba, x):
    wynik = 0
    for num in liczba:
        wynik = wynik * x + int(num)
    return wynik

print(horner("13030", 8))

def decToAll(liczba, x):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % x) + wynik
        liczba //= x
    return wynik

print(decToAll(2, 2))