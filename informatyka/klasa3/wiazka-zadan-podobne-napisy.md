[Wstecz](../informatyka.md)

# Wiązka zadań Podobne napisy

### [Kod](wiazka-zadan-podobne-napisy.py)

```py
def zadanie_72_1(linie):
    licznik = 0
    pierwsza_para = None
    
    for linia in linie:
        a, b = linia.split()
        if len(a) >= 3 * len(b) or len(b) >= 3 * len(a):
            licznik += 1
            if pierwsza_para is None:
                pierwsza_para = (a, b)
    
    return licznik, pierwsza_para

def zadanie_72_2(linie):
    wyniki = []
    
    for linia in linie:
        a, b = linia.split()
        if len(a) < len(b) and b.startswith(a):
            roznica = b[len(a):]
            wyniki.append((a, b, roznica))
    
    return wyniki

def wspolny_koniec(a, b):
    min_dlugosc = min(len(a), len(b))
    licznik = 0
    
    while licznik < min_dlugosc and a[-(licznik+1)] == b[-(licznik+1)]:
        licznik += 1
    
    return licznik

def zadanie_72_3(linie):
    max_dlugosc_konca = 0
    pary = []
    
    for linia in linie:
        a, b = linia.split()
        dlugosc_konca = wspolny_koniec(a, b)
        
        if dlugosc_konca > max_dlugosc_konca:
            max_dlugosc_konca = dlugosc_konca
            pary = [(a, b)]
        elif dlugosc_konca == max_dlugosc_konca:
            pary.append((a, b))
    
    return max_dlugosc_konca, pary

def main():
    with open("napisy.txt", "r") as plik:
        linie = plik.readlines()
    
    wynik_72_1 = zadanie_72_1(linie)
    wynik_72_2 = zadanie_72_2(linie)
    wynik_72_3 = zadanie_72_3(linie)
    
    with open("wyniki.txt", "w") as wyjscie:
        wyjscie.write(f"72.1: {wynik_72_1[0]}\n")
        wyjscie.write(f"Pierwsza para: {wynik_72_1[1]}\n\n")
        
        wyjscie.write("72.2:\n")
        for a, b, roznica in wynik_72_2:
            wyjscie.write(f"{a} {b} {roznica}\n")
        wyjscie.write("\n")
        
        wyjscie.write(f"72.3: Maksymalna dlugosc wspolnego konca: {wynik_72_3[0]}\n")
        for a, b in wynik_72_3[1]:
            wyjscie.write(f"{a} {b}\n")

if __name__ == "__main__":
    main()
```

**[wyniki-podobne-napisy](wyniki-podobne-napisy.txt)**