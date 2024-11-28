[Wstecz](../informatyka.md)

# Wiązka zadań Ciągi arytmetyczne

Ciąg liczb całkowitych nazywamy ciągiem arytmetycznym, jeśli różnica między każdymi dwoma kolejnymi jego wyrazami jest identyczna. Ciągiem arytmetycznym jest na przykład ciąg (1, 3, 5, 7, 9). Jest to ciąg o różnicy 2, ponieważ każdy wyraz tego ciągu, poza pierwszym, różni się od poprzedniego wyrazu o 2. Ciąg (17, 22, 27, 32, 37) jest ciągiem arytmetycznym o różnicy 5. W tym zadaniu rozpatrujemy tylko takie ciągi arytmetyczne, które mają dodatnią różnicę oraz co najmniej pięć wyrazów.

W pliku `ciagi.txt` danych jest 100 ciągów składających się z liczb całkowitych dodatnich, nieprzekraczających 1 000 000. Każdy ciąg opisany jest w dwóch wierszach: pierwszy zawiera liczbę wyrazów ciągu (co najmniej 5 i co najwyżej 1000), zaś drugi — kolejne wyrazy ciągu, oddzielone pojedynczymi odstępami. Dla przykładu pierwsze cztery wiersze pliku mają następującą postać:

5

1 3 6 7 9

5

17 22 27 32 37

Napisz program (lub kilka programów), który wykona podane poniżej polecenia.

### 61.1

Podaj, ile spośród podanych w pliku `ciagi.txt` ciągów jest ciągami arytmetycznymi. Znajdź w śród nich ciąg o największej różnicy i oblicz jego różnicę. Liczbę ciągów arytmetycznych oraz największą różnicę zapisz w pliku `wynik1.txt`.

### 61.2

Dla każdego podanego ciągu znajdź — jeśli istnieje — największą występującą w nim liczbę, która jest pełnym sześcianem jakiejś liczby naturalnej (w pierwszym z przykładowych ciągów jest to $`1 = 1^3`$, w drugim — $`27 = 3^3`$).

Znalezione liczby (po jednej dla każdego ciągu, w którym taka liczba występuje) zapisz w pliku `wynik2.txt`, w kolejności zgodnej z kolejnością ciągów, z których pochodzą.

### 61.3

Plik `bledne.txt` ma identyczną strukturę jak `ciagi.txt`, ale zawiera tylko 20 ciągów. Wiadomo jednak, że wszystkie występujące w nim ciągi są ciągami arytmetycznymi z jednym błędem: jeden z wyrazów w każdym ciągu został zastąpiony przez liczbę naturalną nienależącą do ciągu.

Dla każdego ciągu znajdź i wypisz błędny wyraz. Odpowiedzi zapisz w pliku `wynik3.txt`, podając dla każdego ciągu błędną liczbę w osobnym wierszu, w kolejności zgodnej z kolejnością ciągów w pliku wejściowym.

### [Kod](wiazka-zadan-ciagi-arytmetyczne.py)

```python
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
rozwiaz_61_3(
```

**Odpowiedzi: [wynik1.txt](61/wynik1.txt), [wynik2.txt](61/wynik2.txt), [wynik3.txt](61/wynik3.txt)**
