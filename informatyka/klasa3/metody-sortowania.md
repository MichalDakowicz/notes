[Wstecz](../informatyka.md)

# Metody Sortowania

[Kody](sortowanie.py)

#### Bąbelkowa

```py
def babel(L):
    n = len(L)
    wartownik = False
    for j in range(n-1, 0, -1):
        for i in range(0, j):
            if L[i] > L[i+1]:
                tymczasowa = L[i]
                L[i] = L[i+1]
                L[i+1] = tymczasowa
                wartownik = True
        if wartownik == False:
            break
        wartownik == False

babel(L)
```

#### Szybkie

```py
def szybkie(L, lewy, prawy):
    wyr = lewy
    i = lewy + 1
    j = prawy
    while i <= j:
        while i <= prawy and L[i] < L[wyr]:
            i += 1
        while j >= lewy and L[j] > L[wyr]:
            j -= 1
        if i < j:
            tymczasowa = L[i]
            L[i] = L[j]
            L[j] = tymczasowa
            i += 1
            j -= 1
    tymczasowa = L[wyr]
    L[wyr] = L[j]
    L[j] = tymczasowa
    if j > lewy:
        szybkie(L, lewy, j)
    if i < prawy:
        szybkie(L, i, prawy)

szybkie(L, 0, len(L)-1)
```
