odpowiedz = ""

with open("informatyka/dane/73/tekst.txt") as plik:
    zawartosc_pliku = plik.read().strip()

    liczba_slow_z_podwojna_litera = 0
    slowa = zawartosc_pliku.split()
    for slowo in slowa:
        for i in range(len(slowo) - 1):
            if slowo[i] == slowo[i + 1]:
                liczba_slow_z_podwojna_litera += 1
                break
    odpowiedz += str(liczba_slow_z_podwojna_litera) + "\n"

    czestotliwosc_liter = {}
    for znak in zawartosc_pliku:
        if znak.isalpha():
            if znak in czestotliwosc_liter:
                czestotliwosc_liter[znak] += 1
            else:
                czestotliwosc_liter[znak] = 1

    if 'Z' not in czestotliwosc_liter:
        czestotliwosc_liter['Z'] = 0

    odpowiedz += "Czestotliwosc liter:\n"
    lista_czestotliwosci = sorted(czestotliwosc_liter.items())
    suma_wszystkich_liter = sum(czestotliwosc_liter.values())
    for litera, liczba_wystapien in lista_czestotliwosci:
        procent = round(100 * liczba_wystapien / suma_wszystkich_liter, 2)
        odpowiedz += f"{litera}: {liczba_wystapien} {procent}%\n"

    samogloski = {'A', 'E', 'I', 'O', 'U', 'Y'}
    najdluzszy_ciag_spolglosek = 0
    for slowo in slowa:
        dlugosc_ciagu = 0
        maks_local = 0
        for litera in slowo:
            if litera not in samogloski:
                dlugosc_ciagu += 1
                maks_local = max(maks_local, dlugosc_ciagu)
            else:
                dlugosc_ciagu = 0
        najdluzszy_ciag_spolglosek = max(najdluzszy_ciag_spolglosek, maks_local)
    odpowiedz += str(najdluzszy_ciag_spolglosek) + "\n"

    najdluzsza_sekwencja_spolglosek = 0
    liczba_slow_z_max_sekwencja = 0
    slowo_z_najdluzsza_sekwencja = ""
    for slowo in slowa:
        dlugosc_ciagu = 0
        maks_local = 0
        for litera in slowo:
            if litera not in samogloski:
                dlugosc_ciagu += 1
                maks_local = max(maks_local, dlugosc_ciagu)
            else:
                dlugosc_ciagu = 0
        if maks_local > najdluzsza_sekwencja_spolglosek:
            najdluzsza_sekwencja_spolglosek = maks_local
            liczba_slow_z_max_sekwencja = 1
            slowo_z_najdluzsza_sekwencja = slowo
        elif maks_local == najdluzsza_sekwencja_spolglosek:
            liczba_slow_z_max_sekwencja += 1

    odpowiedz += str(liczba_slow_z_max_sekwencja) + "\n"
    odpowiedz += slowo_z_najdluzsza_sekwencja + "\n"

with open("informatyka/klasa3/73_wyniki.txt", "w") as plik:
    plik.write(odpowiedz)