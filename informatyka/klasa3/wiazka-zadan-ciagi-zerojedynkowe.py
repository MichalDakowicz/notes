def dwucykliczny(ciag):
    d = len(ciag)
    if d % 2 == 1:
        return False
    for j in range(d // 2):
        if ciag[j] != ciag[d // 2 + j]:
            return False
    return True

def dwie_jedynki(ciag):
    for i in range(len(ciag) - 1):
        if ciag[i] == '1' and ciag[i + 1] == '1':
            return False
    return True

def bin2wart(bin):
    w = 0
    for c in bin:
        w = w * 2 + (ord(c) - ord('0'))
    return w

def czy_pierwsza(x):
    if x <= 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x**0.5) + 1, 2):
        if x % i == 0:
            return False
    return True

def czy_polpierwsza(x):
    if czy_pierwsza(x):
        return False
    if x % 2 == 0:
        return czy_pierwsza(x // 2)
    for j in range(3, int(x**0.5) + 1, 2):
        if x % j == 0:
            return czy_pierwsza(x // j)
    return False

with open("informatyka/dane/63/ciagi.txt", "r") as f:
    ciagi = [line.strip() for line in f]

with open("informatyka/klasa3/wyniki_ciagi.txt", "w") as plik:
    plik.write("Dwucykliczne ciągi:\n")
    for ciag in ciagi:
        if dwucykliczny(ciag):
            plik.write(ciag + "\n")

    plik.write("\n")

    ile = sum(1 for ciag in ciagi if dwie_jedynki(ciag))
    plik.write(f"Liczba ciągów niezawierających dwóch sąsiadujących jedynek: {ile}\n\n")

    min_polpierwsza = None
    max_polpierwsza = None
    ile_polpierwszych = 0

    for ciag in ciagi:
        liczba = bin2wart(ciag)
        if czy_polpierwsza(liczba):
            ile_polpierwszych += 1
            if min_polpierwsza is None or liczba < min_polpierwsza:
                min_polpierwsza = liczba
            if max_polpierwsza is None or liczba > max_polpierwsza:
                max_polpierwsza = liczba

    if ile_polpierwszych > 0:
        plik.write(f"Najmniejsza liczba półpierwsza: {min_polpierwsza}\n")
        plik.write(f"Największa liczba półpierwsza: {max_polpierwsza}\n")
        plik.write(f"Liczba półpierwszych: {ile_polpierwszych}\n")
    else:
        plik.write("Brak liczb półpierwszych w danych.\n")
