[Wstecz](../informatyka.md)

# Wiązka zadań Ciągi zerojedynkowe

W pliku ciagi.txt w oddzielnych wierszach znajduje się 1000 różnych ciągów zerojedynkowych, każdy o długości od 2 do 18. Napisz program(-y), który pozwoli rozwiązać poniższe zadania. Następnie je rozwiąż, a odpowiedzi do poszczególnych zadań zapisz w pliku tekstowym wyniki_ciagi.txt. Wyniki do każdego zadania poprzedź numerem oznaczającym to zadanie.

### 63.1.

Ciągiem dwucyklicznym b ędziemy nazywać taki ciąg zerojedynkowy o długości parzystej, który składa się z dwóch fragmentów $`w_1`$ oraz $`w_2`$, $`w=w_1w_2`$, takich że $`w_1=w_2`$. Podaj wszystkie ciągi dwucykliczne zapisane w pliku ciagi.txt.

Przykład

Dla zestawu ciągów:

<u>10010101010011001010101001</u>

11001101001

1001000

<u>11001100</u>

101010011100

<u>110011110011</u>

3 podkreślone ciągi są dwucykliczne.

### 63.2.

Podaj liczbę ciągów z pliku ciagi.txt, w których nie występują obok siebie dwie jedynki.

Przykład

Dla zestawu ciągów:

<u>10101010100101001010010101</u>

11001101001

<u>10001000</u>

101010011100

000011

wynikiem jest liczba 2 (w dwóch podkreślonych ciągach dwie jedynki nie występują obok  
siebie).

### 63.3.

Liczbą półpierwszą nazywamy taką liczbę, która jest iloczynem dwóch liczb pierwszych. Podaj, ile ciągów z pliku ciagi.txt jest reprezentacją binarną liczb półpierwszych. Dodatkowo podaj największą i najmniejszą liczbę półpierwszą w zapisie dziesiętnym.

Przykład

Dla zestawu ciągów:

<u>100010</u>

<u>1101001001</u>

1100101

1111111111

<u>10010110000010010010</u>

podkreślone ciągi są zapisem binarnym liczb półpierwszych, ponieważ:

$`(100010)_2`$ = 34 = 2 \* 17, więc jest liczbą półpierwszą;

$`(1101001001)_2`$ = 841 = 29 \* 29, więc jest liczbą półpierwszą;

$`(1100101)_2`$ = 101 = 101 \* 1;

$`(1111111111)_2`$ = 1023 = 3 _ 11 _ 31;

$`(10010110000010010010)_2`$ = 614546 = 2 \* 307273, więc jest liczbą półpierwszą.

### [Kod](wiazka-zadan-ciagi-zerojedynkowe.py)

```py
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
```

[Wynik](wyniki_ciagi.txt)
