[Wstecz](../informatyka.md)

# Miejsce zerowe f() metodą przybliżenia

### Dane

$`f(x) = 2 \cdot x - 2`$

Przedział $`<a,b>`$

Przybliżenie $`\epsilon = 0.0001`$

### Wyjście

m. zerowe

### Metoda

1. Oblicz $`f(a)`$ i $`f(b)`$
2. Jeśli $`f(a) \cdot f(b) > 0`$ to kończymy
3. Oblicz $`c = \frac{a+b}{2}`$
4. Jeśli $`f(c) = 0`$ to kończymy
5. Jeśli $`f(a) \cdot f(c) < 0`$ to $`b = c`$ w przeciwnym wypadku $`a = c`$
6. Powtarzamy od punktu 3

### [Kod](miejsce-zerowe-f()-metoda-przyblizenia.py)

```python
def f(x):
    return 2 * x - 2

def miejsce_zerowe(a, b, epsilon):
    if f(a) * f(b) > 0:
        return None
    while True:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < epsilon:
            return c

print(miejsce_zerowe(0, 10, 0.0001))
```
