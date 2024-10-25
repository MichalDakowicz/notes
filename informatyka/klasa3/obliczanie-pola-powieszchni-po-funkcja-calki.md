[Wstecz](../informatyka.md)

# Obliczanie pola powierzchni pod funkcją (całki)

**Za pomocą metod numerycznych oblicz pole powierzchni pod wykresem funkcji w przedziale <a,b> z dokładnością E=1000.**

### Dane

$`y=f(x)=x^2+1`$

$`\Epsilon=1000`$ -> il. prostokątów (im więcej tym bliższe przybliżenie)

$`a=0`$

$`b=4`$

$`x=\frac{b-a}{\Epsilon}`$

### Wyjście

-   pole powierzchni całki

### Metoda

1. Obliczamy $`x`$ -> $`\frac{b-a}{\Epsilon}`$
2. Dla każdego $`i`$ z przedziału $`<0,\Epsilon>`$ obliczamy $`f(x_i)`$ i mnożymy przez $`x`$
3. Dodajemy wynik do pola powierzchni
4. Zwracamy wartość

### [Kod](obliczanie-pola-powieszchni-po-funkcja-calki.py)

```python
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

def calka_trapez(a, b, epsilon):
    x = (b-a)/epsilon
    pole = 0
    for i in range(epsilon):
        y1 = f(a+i*x)
        y2 = f(a+(i+1)*x)
        pole += (y1+y2)*x/2
    return pole

print(calka_trapez(0, 4, 100))
```
