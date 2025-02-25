def czy_jednolity(napis):
    return all(znak == napis[0] for znak in napis)

def czy_anagramy(napis1, napis2):
    return sorted(napis1) == sorted(napis2)

def policz_jednolite_anagramy(pary):
    return sum(1 for napis1, napis2 in pary if czy_jednolity(napis1) and napis1 == napis2)

def policz_pary_anagramow(pary):
    return sum(1 for napis1, napis2 in pary if czy_anagramy(napis1, napis2))

def najwieksza_grupa_anagramow(pary):
    wszystkie_napisy = [napis for para in pary for napis in para]
    licznik = {}
    
    for napis in wszystkie_napisy:
        klucz = tuple(sorted(napis))
        licznik[klucz] = licznik.get(klucz, 0) + 1
    
    return max(licznik.values())

def wczytaj_dane(nazwa_pliku):
    with open(nazwa_pliku, 'r') as plik:
        return [wiersz.strip().split() for wiersz in plik]

def zapisz_wyniki(nazwa_pliku, wyniki):
    with open(nazwa_pliku, 'w') as plik:
        for klucz, wartosc in wyniki.items():
            plik.write(f"{klucz}: {wartosc}\n")

dane = wczytaj_dane("informatyka/dane/68/dane_napisy.txt")

wyniki = {
    "68.1": policz_jednolite_anagramy(dane),
    "68.2": policz_pary_anagramow(dane),
    "68.3": najwieksza_grupa_anagramow(dane)
}

zapisz_wyniki("informatyka/klasa3/wyniki_anagramy.txt", wyniki)
