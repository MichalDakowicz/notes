[Wstecz](../informatyka.md)

# Metody numeryczne

### Dane

$`\epsilon=0.001`$ - przybliżenie

P - liczba

$`a=\frac{a+a'}{2}`$

$`a'=\frac{P}{a}`$

### Wyjście

$`\sqrt{P}`$ -> a lub a'

### Metoda

1. Przypisz a=1
2. Przypisz a'=P
3. Dopóki $`|a-a'|>\epsilon`$ wykonuj:
    1. $`a=\frac{a+a'}{2}`$
    2. $`a'=\frac{P}{a}`$
4. Zwróć a

### [Kod](metody-numeryczne.py)

```python
def pierwiastek(P, epsilon):
    a = 1
    a_prim = P
    while abs(a - a_prim) > epsilon:
        a = (a + a_prim) / 2
        a_prim = P / a
    return a

print(pierwiastek(4, 0.001))
```
