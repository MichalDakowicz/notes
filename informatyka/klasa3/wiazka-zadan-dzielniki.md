[Wstecz](../informatyka.md)

# Wiązka zadań Dzielniki

W pliku liczby.txt danych jest 200 różnych liczb całkowitych z przedziału $`[2, 1 000 000]`$, każda w osobnym wierszu pliku. Napisz program (lub kilka programów), który poda odpowiedzi do poniższych zadań. Odpowiedzi zapisz do pliku wyniki.txt

### 60.1

Policz, ile jest w pliku wejściowym liczb mniejszych niż 1000, oraz podaj dwie takie liczby, które pojawiają się w pliku jako ostatnie (możesz założyć, że będą co najmniej dwie).

### 60.2

Wśród liczb występujących w pliku wejściowym znajdź te, które mają dokładnie 18 dzielników naturalnych (wliczając w nie 1 i samą liczbę). Dla każdej znalezionej liczby wypisz, oprócz jej wartości, listę wszystkich jej dzielników, posortowaną rosnąco.

### 60.3

Znajdź największą liczbę w pliku, która jest względnie pierwsza ze wszystkimi pozostałymi, czyli taką, która z żadną z pozostałych liczb nie ma wspólnego dzielnika innego niż 1.

### [Kod](wiazka-zadan-dzielniki.py)

```python
liczby = []
with open("informatyka/dane/60/liczby.txt", "r") as plik:
    for line in plik.readlines():
        liczby.append(int(line))

# 60.1
wieksze_1000 = []
ilosc = 0

for liczba in liczby:
    if liczba < 1000:
        wieksze_1000.append(liczba)
        ilosc += 1

# 60.2
liczby_18_dzielnikow = {}

for liczba in liczby:
    ilosc_dzielnikow = 0
    dzielniki = []
    for dzielnik in range(1, int((liczba + 1)**0.5)):
        if liczba % dzielnik == 0:
            ilosc_dzielnikow += 2
            dzielniki.append(dzielnik)
            dzielniki.append(liczba // dzielnik)
    if ilosc_dzielnikow == 18:
        liczby_18_dzielnikow[liczba] = sorted(dzielniki)

# 60.3
def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def czy_wzglednie_pierwsza_z_wszystkimi(liczba, liczby):
    for inna_liczba in liczby:
        if inna_liczba != liczba and nwd(liczba, inna_liczba) != 1:
            return False
    return True

najwieksza_wzglednie_pierwsza = None
for liczba in sorted(liczby, reverse=True):
    if czy_wzglednie_pierwsza_z_wszystkimi(liczba, liczby):
        najwieksza_wzglednie_pierwsza = liczba
        break


with open("informatyka/klasa3/zadanie_dzielniki.txt", "w") as plik:
    plik.write("60.1 " + str(ilosc) + ", 2 ostatnie: " + str(wieksze_1000[-2:]) + "\n")
    plik.write("60.2 " + str(liczby_18_dzielnikow) + "\n")
    plik.write("60.3 " + str(najwieksza_wzglednie_pierwsza) + "\n")
```

**Odpowiedzi: [zadanie_dzielniki.txt](zadanie_dzielniki.txt)**
