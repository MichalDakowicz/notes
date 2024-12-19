# Zadanie 1

najwieksza = 0
najmniejsza = 9999999999999

def horner(liczba, x):
    wynik = 0
    for num in liczba:
        wynik = wynik * x + int(num)
    return wynik

with open("informatyka/dane/62/liczby1.txt") as file:
    liczby = file.readlines()

for linia in liczby:
    liczba = int(linia.strip(), 8)
    if liczba > najwieksza:
        najwieksza = liczba
    if liczba < najmniejsza:
        najmniejsza = liczba

# Zadanie 2

ciag_niemalejacy = []
najdluzszy_ciag = []

with open("informatyka/dane/62/liczby2.txt") as file:
    liczby = file.readlines()

for linia in liczby:
    liczba = int(linia.strip())
    if not ciag_niemalejacy or liczba >= ciag_niemalejacy[-1]:
        ciag_niemalejacy.append(liczba)
    else:
        if len(ciag_niemalejacy) > len(najdluzszy_ciag):
            najdluzszy_ciag = ciag_niemalejacy
        ciag_niemalejacy = [liczba]
if len(ciag_niemalejacy) > len(najdluzszy_ciag):
    najdluzszy_ciag = ciag_niemalejacy

# Zadanie 3

licznik_a = 0
licznik_b = 0
with open("informatyka/dane/62/liczby1.txt") as file, open("informatyka/dane/62/liczby2.txt") as file2:
    liczby1 = file.readlines()
    liczby2 = file2.readlines()

for i in range(len(liczby1)):
    liczba1 = int(liczby1[i].strip(), 8)
    liczba2 = int(liczby2[i].strip())
    if liczba1 == liczba2:
        licznik_a += 1
    elif liczba1 > liczba2:
        licznik_b += 1

# Zadanie 4

def policz_szesci():
    licznik_szostek_dziesietnych = 0
    licznik_szostek_osemkowych = 0

    with open("informatyka/dane/62/liczby2.txt", "r") as file:
        for linia in file:
            wartosc_dziesietna = linia.strip()
            licznik_szostek_dziesietnych += wartosc_dziesietna.count("6")

            wartosc_osemkowa = oct(int(wartosc_dziesietna)).lstrip("0o")
            licznik_szostek_osemkowych += wartosc_osemkowa.count("6")

    return licznik_szostek_dziesietnych, licznik_szostek_osemkowych

licznik_szostek_dziesietnych, licznik_szostek_osemkowych = policz_szesci()

with open("informatyka/klasa3/62/zadanie-liczby-osemkowe.txt", "w") as file:
    file.write("Zadanie 1\n")
    file.write(f"Największa liczba w ósemkowym: {oct(najwieksza).lstrip('0o')}\n")
    file.write(f"Najmniejsza liczba w ósemkowym: {oct(najmniejsza).lstrip('0o')}\n")
    file.write("\nZadanie 2\n")
    file.write(f"Najdłuższy niemalejący ciąg liczb rozpoczyna się liczbą {najdluzszy_ciag[0]} i składa się z {len(najdluzszy_ciag)} elementów.\n")
    file.write("\nZadanie 3\n")
    file.write(f"a) Liczba wierszy z taką samą wartością: {licznik_a}\n")
    file.write(f"b) Liczba wierszy, gdzie liczba z liczby1.txt jest większa: {licznik_b}\n")
    file.write("\nZadanie 4\n")
    file.write(f"Cyfra 6 w systemie dziesiętnym: {licznik_szostek_dziesietnych}\n")
    file.write(f"Cyfra 6 w systemie ósemkowym: {licznik_szostek_osemkowych}\n")
