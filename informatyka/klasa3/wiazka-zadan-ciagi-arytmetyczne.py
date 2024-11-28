def rozwiaz_61_1():
    with open("informatyka/dane/61/ciagi.txt", "r") as plik:
        linie = plik.readlines()
    
    liczba_ciagow_arytmetycznych = 0
    maksymalna_roznica = 0
    
    for i in range(0, len(linie), 2):
        n = int(linie[i].strip())
        ciag = list(map(int, linie[i + 1].strip().split()))
        
        czy_arytmetyczny = True
        roznica = ciag[1] - ciag[0]
        
        for j in range(2, n):
            if ciag[j] - ciag[j - 1] != roznica:
                czy_arytmetyczny = False
                break
        
        if czy_arytmetyczny:
            liczba_ciagow_arytmetycznych += 1
            maksymalna_roznica = max(maksymalna_roznica, roznica)
    
    with open("informatyka/klasa3/61/wynik1.txt", "w") as plik_wynikowy:
        plik_wynikowy.write(str(liczba_ciagow_arytmetycznych) + "\n")
        plik_wynikowy.write(str(maksymalna_roznica) + "\n")

def rozwiaz_61_2():
    with open("informatyka/dane/61/ciagi.txt", "r") as plik:
        linie = plik.readlines()
    
    szesciany = []
    
    for i in range(0, len(linie), 2):
        ciag = list(map(int, linie[i + 1].strip().split()))
        maksymalny_szescian = 0
        
        for liczba in ciag:
            for j in range(1, int(liczba**(1/3)) + 2):
                if j**3 == liczba:
                    maksymalny_szescian = max(maksymalny_szescian, liczba)
                    break
        
        if maksymalny_szescian > 0:
            szesciany.append(maksymalny_szescian)
    
    with open("informatyka/klasa3/61/wynik2.txt", "w") as plik_wynikowy:
        for szescian in szesciany:
            plik_wynikowy.write(str(szescian) + "\n")

def rozwiaz_61_3():
    with open("informatyka/dane/61/bledne.txt", "r") as plik:
        linie = plik.readlines()
    
    bledy = []
    
    for i in range(0, len(linie), 2):
        n = int(linie[i].strip())
        ciag = list(map(int, linie[i + 1].strip().split()))
        
        roznica = ciag[1] - ciag[0]
        indeks_bledu = -1
        
        for j in range(2, n):
            if ciag[j] - ciag[j - 1] != roznica:
                if indeks_bledu == -1:
                    if j + 1 < n and ciag[j+1] - ciag[j-1] == 2*roznica:
                        indeks_bledu = j
                    elif j > 0:
                        indeks_bledu = j - 1
                break

        if indeks_bledu != -1:
          bledy.append(ciag[indeks_bledu])
        else:
            print("Nie znaleziono błędu w ciągu:", ciag)

    with open("informatyka/klasa3/61/wynik3.txt", "w") as plik_wynikowy:
        for blad in bledy:
            plik_wynikowy.write(str(blad) + "\n")

rozwiaz_61_1()
rozwiaz_61_2()
rozwiaz_61_3()