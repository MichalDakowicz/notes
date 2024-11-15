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