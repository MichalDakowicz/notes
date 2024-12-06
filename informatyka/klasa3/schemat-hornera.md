[Wstecz](../informatyka.md)

# Schemat Hornera

### Dane

#### Horner:

-   liczba w wybranym systemie

-   system liczby

#### decToAll:

-   liczba w systemie dziesiętnym

-   system do przeliczenia

### Wyjście

#### Horner:

-   liczba w systemie dziesiętnym

#### decToAll:

-   liczba w wybranym systemie

### [Kod](schemat-hornera.py)

```py
def horner(liczba, x):
    wynik = 0
    for num in liczba:
        wynik = wynik * x + int(num)
    return wynik

print(horner("13030", 8))

def decToAll(liczba, x):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba % x) + wynik
        liczba //= x
    return wynik

print(decToAll(2, 2))
```
