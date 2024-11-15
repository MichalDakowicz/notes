[Wstecz](../informatyka.md)

# Wiązka zadań Zasłona

Pani Binarna dostała zlecenie na uszycie zasłony. Na rysunku poniżej przedstawiono zasłonę, która jest ograniczona:

-   od góry prostą $`y=19\frac{61}{125}`$,
-   od dołu prostą $`y=-32\frac{2}{3}`$,
-   z lewej strony prostą $`x=2`$
-   z prawej strony dwoma krzywymi: $`f(x)=\frac{x^4}{500}-\frac{x^2}{200}-\frac{3}{250}`$ oraz $`g(x)=-\frac{x^3}{30}+\frac{x}{20}+\frac{1}{6}`$

**Uwaga:** Zauważ, że $`f(10)=19\frac{61}{125}`$, zaś $`g(10)=-32\frac{2}{3}`$

![](zaslona-pomocniczy-1.png)

Korzystając z dostępnych narzędzi informatycznych, wykonaj poniższe zadania. Odpowiedzi do nich umieść w pliku `zadanie_zaslona.txt`. Każda odpowiedź powinna być poprzedzona numerem je oznaczającym.

### 70.1

Pani Binarna zakupiła tyle materiału, ile wynosi pole prostokąta ABCD, w którym mieści się zasłona. Oblicz, jaka będzie powierzchnia materiału pozostałego po wykrojeniu zasłony. Wynik podaj z dokładnością do 1/1000.

### 70.2

Pani Binarna zamierza obszyć taśmą zasłonę ze wszystkich czterech stron, w tym celu chce wyznaczyć obwód zasłony. Część obwodu ograniczoną wykresem funkcji f(x) szacujemy w następujący sposób: Odcinek $`[2,10]`$ dzielimy na 1000 równych części, których prawe końce oznaczamy przez $`x_1,...,x_{1000}`$. Długość krzywej odpowiadającej wykresowi $`f(x)`$ na przedziale $`[2,10]`$ przybliżamy długością łamanej łączącej punkty $`(2, f(2)), (x1, f(x1)), (x2, f(x2))`$ itd. aż do $`(x_{1000}, f(x_{1000}))`$. Analogicznie wyznaczamy część obwodu ograniczoną przez $`g(x)`$.

Stosując powyższą metodę wyznaczania obwodu, oblicz długość taśmy, jaką musi zakupić pani Binarna, zakładając, że w sprzedaży jest tylko taśma o długościach będących wielokrotnością jednego metra.

### 70.3

Pani Binarna postanowiła wykorzystać pozostały fragment materiału i wyciąć z niego pasy o szerokości 0,25 m i o bokach równoległych do osi układu współrzędnych. Podaj sumę długości pasów, które można wyciąć z pozostałego fragmentu materiału. Załóż, że długość każdego wyciętego pasa jest liczbą całkowitą oraz że pani Binarna zaczyna wycinać pasy od prawej strony materiału

![](zaslona-pomocniczy-2.png)

### Pomoce

**CAŁKA**

```py
def f(x):
    return x*x+1

def calka(a, b, epsilon):
    x = (b-a)/epsilon
    pole = 0
    for i in range(epsilon):
        y = f(a+i*x)
        pole += y*x
    return pole

print(calka(0, 4, 1000))
```

### [Kod](wiazka-zadan-zaslona.py)

```python
def f(x):
    return (x**4) / 500 - (x**2) / 200 - 3 / 250

def g(x):
    return -(x**3) / 30 + x / 20 + 1 / 6

def calka(func, a, b, epsilon):
    x = (b - a) / epsilon
    pole = 0
    for i in range(epsilon):
        y = func(a + i * x)
        pole += y * x
    return pole

def przyblizenie_gora(x):
    if int(x) == x:
        return int(x)
    else:
        return int(x) + 1


# 70.1
y_gorna = 19 + 61/125
y_dolna = -32 - 2/3
x_lewa = 2
x_prawa = 10

pole_prostokata = (y_gorna - y_dolna) * (x_prawa - x_lewa)
pole_zaslony = calka(f, 2, 10, 1000) - calka(g, 2, 10, 1000)
pozostaly_material = pole_prostokata - pole_zaslony

# 70.2
def dlugosc_krzywej(func, a, b, n):
    dx = (b - a) / n
    dlugosc = 0
    for i in range(n):
        x1 = a + i * dx
        x2 = x1 + dx
        y1 = func(x1)
        y2 = func(x2)
        dlugosc += ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return dlugosc

obwod_f = dlugosc_krzywej(f, 2, 10, 1000)
obwod_g = dlugosc_krzywej(g, 2, 10, 1000)
obwod_zaslony = obwod_f + obwod_g + (y_gorna - y_dolna) + (y_gorna - y_dolna) # Dodajemy dwa boki pionowe
tasma = przyblizenie_gora(obwod_zaslony)

# 70.3
szerokosc_pasa = 0.25
suma_dlugosci_pasow = 0
y_rozmiar = y_gorna - y_dolna

liczba_pasow = int(y_rozmiar // szerokosc_pasa)

for i in range(liczba_pasow):
    y_gora_pasa = y_gorna - i * szerokosc_pasa
    y_dol_pasa = y_gora_pasa - szerokosc_pasa

    x_lewy_f = 2
    x_prawy_f = 10
    x_lewy_g = 2
    x_prawy_g = 10

    dlugosc_pasa = int(x_prawy_f - x_lewy_g)
    suma_dlugosci_pasow += dlugosc_pasa


with open("informatyka/klasa3/zadanie_zaslona.txt", "w") as plik:
    plik.write("70.1 " + str(round(pozostaly_material, 3)) + "\n")
    plik.write("70.2 " + str(tasma) + "\n")
    plik.write("70.3 " + str(suma_dlugosci_pasow) + "\n")
```

**Odpowiedzi: [zadanie_zaslona.txt](zadanie_zaslona.txt)**
