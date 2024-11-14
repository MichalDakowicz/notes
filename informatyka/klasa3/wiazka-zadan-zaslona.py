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


with open("zadanie_zaslona.txt", "w") as plik:
    plik.write("70.1 " + str(round(pozostaly_material, 3)) + "\n")
    plik.write("70.2 " + str(tasma) + "\n")
    plik.write("70.3 " + str(suma_dlugosci_pasow) + "\n")