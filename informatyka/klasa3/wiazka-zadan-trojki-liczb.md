[Wstecz](../informatyka.md)

# Wiązka zadań Trójki liczb

### [Kod](wiazka-zadan-trojki-liczb.py)

```py
def suma_cyfr(n):
    return sum(int(c) for c in str(n))

def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def czy_prostokatny(a, b, c):
    return (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a)

def czy_trojkat(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

def zadanie_66():
    with open("informatyka/dane/66/trojki.txt", "r") as f, open("informatyka/klasa3/wyniki_trojki.txt", "w") as w:
        trojki = [list(map(int, line.split())) for line in f]
        
        w.write("66.1\n")
        for a, b, c in trojki:
            if suma_cyfr(a) + suma_cyfr(b) == c:
                w.write(f"{a} {b} {c}\n")
        
        w.write("\n66.2\n")
        for a, b, c in trojki:
            if pierwsza(a) and pierwsza(b) and a * b == c:
                w.write(f"{a} {b} {c}\n")
        
        w.write("\n66.3\n")
        for i in range(len(trojki) - 1):
            if czy_prostokatny(*trojki[i]) and czy_prostokatny(*trojki[i + 1]):
                w.write(f"{trojki[i][0]} {trojki[i][1]} {trojki[i][2]}\n")
                w.write(f"{trojki[i + 1][0]} {trojki[i + 1][1]} {trojki[i + 1][2]}\n\n")
        
        w.write("66.4\n")
        licznik = 0
        dlugosc = 0
        max_dlugosc = 0
        for a, b, c in trojki:
            if czy_trojkat(a, b, c):
                licznik += 1
                dlugosc += 1
                max_dlugosc = max(max_dlugosc, dlugosc)
            else:
                dlugosc = 0
        w.write(f"{licznik}\n{max_dlugosc}\n")

zadanie_66()

```

**[Wyniki](wyniki_trojki.txt)**

