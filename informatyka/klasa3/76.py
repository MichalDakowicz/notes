def szyfruj_50(napis, klucz):
    napis = list(napis)
    for i in range(50):
        a, b = i, klucz[i] - 1
        napis[a], napis[b] = napis[b], napis[a]
    return ''.join(napis)

with open('informatyka/dane/76/szyfr1.txt') as plik:
    linie = plik.read().splitlines()
    napisy = linie[:6]
    klucz = list(map(int, linie[6].split()))

wyniki = [szyfruj_50(napis, klucz) for napis in napisy]

for wynik in wyniki:
    print(wynik + "\n")

def szyfruj_modulo(napis, klucz):
    napis = list(napis)
    dlugosc = len(klucz)
    for i in range(len(napis)):
        a, b = i, klucz[i % dlugosc] - 1
        napis[a], napis[b] = napis[b], napis[a]
    return ''.join(napis)

with open('informatyka/dane/76/szyfr2.txt') as plik:
    linie = plik.read().splitlines()
    napis = linie[0]
    klucz = list(map(int, linie[1].split()))

wynik = szyfruj_modulo(napis, klucz)

print(wynik)

def deszyfruj(napis, klucz):
    napis = list(napis)
    dlugosc = len(klucz)
    for i in range(49, -1, -1):
        a, b = i, klucz[i % dlugosc] - 1
        napis[a], napis[b] = napis[b], napis[a]
    return ''.join(napis)

with open('informatyka/dane/76/szyfr3.txt') as plik:
    napis = plik.read().strip()

klucz = [6, 2, 4, 1, 5, 3]
wynik = deszyfruj(napis, klucz)

print(wynik)
