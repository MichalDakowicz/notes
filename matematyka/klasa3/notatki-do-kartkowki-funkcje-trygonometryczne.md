[Wstecz](../matematyka.md)

# Notatki do kartkówki - Funkcje trygonometryczne

### 1. Zamiana stopnie na radiany i odwrotnie

-   **Stopnie na radiany:** Mnożymy miarę kąta w stopniach przez $`\frac{\pi}{180\degree}`$. Np. $`30\degree$ to $30\degree \cdot \frac{\pi}{180\degree} = \frac{\pi}{6}`$ radianów.

-   **Radiany na stopnie:** Mnożymy miarę kąta w radianach przez $`\frac{180\degree}{\pi}`$. Np. $`\frac{\pi}{3}`$ radianów to $`\frac{\pi}{3} \cdot \frac{180\degree}{\pi} = 60\degree`$.

-   **Wartości kluczowe:** Zapamiętaj zamianę dla kątów: $`0\degree`$, $`30\degree`$, $`45\degree`$, $`60\degree`$, $`90\degree`$, $`180\degree`$, $`270\degree`$, $`360\degree`$.

### 2. Okresowość funkcji trygonometrycznych

-   **Definicja:** Funkcja $`f(x)`$ jest okresowa z okresem $`T`$ jeśli dla każdego $`x`$ z dziedziny funkcji zachodzi $`f(x+T) = f(x)`$.

-   **Okresy podstawowe:**

    -   $`\sin(x)`$ i $`\cos(x)`$ mają okres $`2\pi`$: $`\sin(x + 2\pi) = \sin(x)`$ i $`\cos(x + 2\pi) = \cos(x)`$.
    -   $`\tg(x)`$ i $`\ctg(x)`$ mają okres $`\pi`$: $`\tg(x + \pi) = \tg(x)`$ i $`\ctg(x + \pi) = \ctg(x)`$.

-   **Wykorzystanie okresowości:** Pozwala uprościć obliczanie wartości funkcji trygonometrycznych dla kątów spoza przedziału $`[0, 2\pi]`$ (lub $`[0, \pi]`$ dla tangensa i cotangensa). Np. $`\sin(3\pi) = \sin(3\pi - 2\pi) = \sin(\pi) = 0`$.

### 3. Wzory redukcyjne

-   **Idea:** Wzory redukcyjne pozwalają sprowadzić funkcje trygonometryczne dowolnego kąta do funkcji kąta ostrego.

-   **Kąty $`\frac{\pi}{2} \pm \alpha`$, $`\pi \pm \alpha`$, $`\frac{3\pi}{2} \pm \alpha`$, $`2\pi \pm \alpha`$:**

    -   **Zmiana funkcji:** Jeśli kąt ma postać $`\frac{\pi}{2} \pm \alpha`$ lub $`\frac{3\pi}{2} \pm \alpha`$, funkcja zmienia się na kofunkcję (sinus na cosinus, tangens na cotangens itd.). Jeśli kąt ma postać $`\pi \pm \alpha`$ lub $`2\pi \pm \alpha`$, funkcja pozostaje bez zmian.

    -   **Znak:** Znak wynikowej funkcji zależy od ćwiartki, w której leży kąt wyjściowy. Np., $`\sin(\pi - \alpha) = \sin(\alpha)`$, $`\cos(\pi + \alpha) = -\cos(\alpha)`$, $`\tg(\frac{3\pi}{2} + \alpha) = -\ctg(\alpha)`$.

-   **Przykład:** $`\cos(\frac{3\pi}{2} - \alpha)`$. Kąt $`\frac{3\pi}{2} - \alpha`$ leży w III ćwiartce, gdzie cosinus jest ujemny. Funkcja zmienia się na sinus. Zatem $`\cos(\frac{3\pi}{2} - \alpha) = -\sin(\alpha)`$.

$`\mathrm{tg}`$