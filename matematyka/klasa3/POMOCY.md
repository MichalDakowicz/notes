**Grupa A**

**1** Ile punktów wspólnych mają okręgi $x^2+(y-1)^2=1 \mathrm{i}(x-4)^2+(y-4)^2=9$ ?
A. 0 B. 1 C. 2 D. 3

Okrąg 1: $x^2+(y-1)^2=1$
Środek $S_1 = (0, 1)$, promień $r_1 = \sqrt{1} = 1$.
Okrąg 2: $(x-4)^2+(y-4)^2=9$
Środek $S_2 = (4, 4)$, promień $r_2 = \sqrt{9} = 3$.

Odległość między środkami okręgów:
$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$
$d = \sqrt{(4-0)^2 + (4-1)^2} = \sqrt{4^2 + 3^2} = \sqrt{16+9} = \sqrt{25} = 5$.

Suma promieni: $r_1 + r_2 = 1 + 3 = 4$.
Wartość bezwzględna różnicy promieni: $|r_1 - r_2| = |1 - 3| = |-2| = 2$.

Porównanie $d$ z $r_1+r_2$ i $|r_1-r_2|$:
$d = 5$
$r_1+r_2 = 4$
$|r_1-r_2| = 2$
Ponieważ $d > r_1+r_2$ (czyli $5 > 4$), okręgi są rozłączne zewnętrznie. Mają 0 punktów wspólnych.

Odpowiedź: A. 0

**2** Okrąg o środku w punkcie $A(-4,5)$ przechodzi przez punkt $P(-1,10)$, a okrąg o środku $B(-6,1)$ przez punkt $Q(-8,-2)$. Wyznacz równania tych okręgów i określ ich wzajemne położenie.

Okrąg o środku $A(-4,5)$ przechodzący przez $P(-1,10)$:
Promień $r_A = \sqrt{(-1 - (-4))^2 + (10 - 5)^2} = \sqrt{(-1+4)^2 + 5^2} = \sqrt{3^2 + 5^2} = \sqrt{9+25} = \sqrt{34}$.
Równanie okręgu 1: $(x - (-4))^2 + (y - 5)^2 = (\sqrt{34})^2 \Rightarrow (x+4)^2 + (y-5)^2 = 34$.

Okrąg o środku $B(-6,1)$ przechodzący przez $Q(-8,-2)$:
Promień $r_B = \sqrt{(-8 - (-6))^2 + (-2 - 1)^2} = \sqrt{(-8+6)^2 + (-3)^2} = \sqrt{(-2)^2 + (-3)^2} = \sqrt{4+9} = \sqrt{13}$.
Równanie okręgu 2: $(x - (-6))^2 + (y - 1)^2 = (\sqrt{13})^2 \Rightarrow (x+6)^2 + (y-1)^2 = 13$.

Wzajemne położenie okręgów:
Środki: $S_A = (-4,5)$, $S_B = (-6,1)$.
Promienie: $r_A = \sqrt{34}$, $r_B = \sqrt{13}$.
Odległość między środkami:
$d(A,B) = \sqrt{(-6 - (-4))^2 + (1 - 5)^2} = \sqrt{(-2)^2 + (-4)^2} = \sqrt{4+16} = \sqrt{20}$.

Suma promieni: $r_A + r_B = \sqrt{34} + \sqrt{13}$.
$(\sqrt{34} + \sqrt{13})^2 = 34 + 13 + 2\sqrt{34 \cdot 13} = 47 + 2\sqrt{442}$.
Wartość bezwzględna różnicy promieni: $|r_A - r_B| = |\sqrt{34} - \sqrt{13}|$.
$(|\sqrt{34} - \sqrt{13}|)^2 = (\sqrt{34} - \sqrt{13})^2 = 34 + 13 - 2\sqrt{34 \cdot 13} = 47 - 2\sqrt{442}$.
$d(A,B)^2 = (\sqrt{20})^2 = 20$.

Porównujemy:
$|r_A - r_B|^2 = 47 - 2\sqrt{442} \approx 47 - 2 \cdot 21.02 = 47 - 42.04 = 4.96$.
$d(A,B)^2 = 20$.
$(r_A + r_B)^2 = 47 + 2\sqrt{442} \approx 47 + 42.04 = 89.04$.
Mamy $4.96 < 20 < 89.04$, więc $|r_A - r_B|^2 < d(A,B)^2 < (r_A + r_B)^2$.
Ponieważ promienie i odległość są dodatnie, to $|r_A - r_B| < d(A,B) < r_A + r_B$.
Okręgi przecinają się w dwóch punktach.

Równania okręgów: $(x+4)^2 + (y-5)^2 = 34$ i $(x+6)^2 + (y-1)^2 = 13$.
Wzajemne położenie: Okręgi przecinają się w dwóch punktach.

**3** Jaka jest odległość między środkami okręgów o promieniach 9 i 3, jeśli te okręgi są wewnętrznie styczne?
A. 3 B. 6 C. 9 D. 12

Promienie okręgów: $r_1 = 9$, $r_2 = 3$.
Okręgi są wewnętrznie styczne, więc odległość między ich środkami jest równa wartości bezwzględnej różnicy ich promieni.
$d = |r_1 - r_2| = |9 - 3| = 6$.

Odpowiedź: B. 6

**4** Jaka musi być odległość $d$ między środkami okręgów o promieniach 3 i 5, aby te okręgi były rozłączne?

Promienie okręgów: $r_1 = 3$, $r_2 = 5$.
Aby okręgi były rozłączne, odległość $d$ między ich środkami musi spełniać jeden z warunków:

1.  Rozłączne zewnętrznie: $d > r_1 + r_2$.
    $d > 3 + 5 \Rightarrow d > 8$.
2.  Rozłączne wewnętrznie (jeden okrąg wewnątrz drugiego, bez punktów wspólnych): $d < |r_1 - r_2|$.
    $d < |3 - 5| \Rightarrow d < |-2| \Rightarrow d < 2$.
    Ponieważ odległość $d$ musi być nieujemna ($d \ge 0$), warunek to $0 \le d < 2$.

Odpowiedź: Odległość $d$ musi spełniać warunek $d > 8$ lub $0 \le d < 2$.

**5** Wyznacz wszystkie wartości parametru $k$, dla których okręgi $O_1$ i $O_2$ są styczne, jeśli

$$
\begin{aligned}
& O_1: x^2+y^2-6 x+2 y=0 \\
& O_2: x^2+y^2+12 x-8 y+52-k=0
\end{aligned}
$$

Okrąg $O_1: x^2+y^2-6 x+2 y=0$.
Przekształcamy do postaci kanonicznej:
$(x^2-6x) + (y^2+2y) = 0$
$(x^2-6x+9) - 9 + (y^2+2y+1) - 1 = 0$
$(x-3)^2 + (y+1)^2 = 10$.
Środek $S_1 = (3,-1)$, promień $r_1 = \sqrt{10}$.

Okrąg $O_2: x^2+y^2+12 x-8 y+52-k=0$.
Przekształcamy do postaci kanonicznej:
$(x^2+12x) + (y^2-8y) = k-52$
$(x^2+12x+36) - 36 + (y^2-8y+16) - 16 = k-52$
$(x+6)^2 + (y-4)^2 = k-52+36+16$
$(x+6)^2 + (y-4)^2 = k$.
Środek $S_2 = (-6,4)$, promień $r_2 = \sqrt{k}$.
Aby $O_2$ był okręgiem, musi zachodzić $k>0$.

Odległość między środkami $S_1$ i $S_2$:
$d = \sqrt{(-6-3)^2 + (4-(-1))^2} = \sqrt{(-9)^2 + (4+1)^2} = \sqrt{81+5^2} = \sqrt{81+25} = \sqrt{106}$.

Okręgi są styczne, jeśli $d = r_1+r_2$ (styczne zewnętrznie) lub $d = |r_1-r_2|$ (styczne wewnętrznie).

Przypadek 1: Styczne zewnętrznie ($d = r_1+r_2$)
$\sqrt{106} = \sqrt{10} + \sqrt{k}$
$\sqrt{k} = \sqrt{106} - \sqrt{10}$.
Ponieważ $106 > 10$, to $\sqrt{106} > \sqrt{10}$, więc $\sqrt{106} - \sqrt{10} > 0$.
Podnosząc do kwadratu: $k = (\sqrt{106} - \sqrt{10})^2 = 106 + 10 - 2\sqrt{106 \cdot 10} = 116 - 2\sqrt{1060}$.
$1060 = 4 \cdot 265$, więc $2\sqrt{1060} = 2\sqrt{4 \cdot 265} = 2 \cdot 2\sqrt{265} = 4\sqrt{265}$.
$k = 116 - 4\sqrt{265}$.
Sprawdzenie $k>0$: $116 - 4\sqrt{265} > 0 \Rightarrow 116 > 4\sqrt{265} \Rightarrow 29 > \sqrt{265}$.
$29^2 = 841$, $(\sqrt{265})^2 = 265$. Ponieważ $841 > 265$, warunek $k>0$ jest spełniony.

Przypadek 2: Styczne wewnętrznie ($d = |r_1-r_2|$)
$\sqrt{106} = |\sqrt{10} - \sqrt{k}|$.
To równanie rozbijamy na dwa przypadki:
a) $\sqrt{10} - \sqrt{k} = \sqrt{106}$
$\sqrt{k} = \sqrt{10} - \sqrt{106}$.
Ponieważ $\sqrt{10} < \sqrt{106}$, prawa strona jest ujemna. To równanie nie ma rozwiązania, ponieważ $\sqrt{k} \ge 0$.

b) $\sqrt{10} - \sqrt{k} = -\sqrt{106}$
$\sqrt{k} = \sqrt{10} + \sqrt{106}$.
Podnosząc do kwadratu: $k = (\sqrt{10} + \sqrt{106})^2 = 10 + 106 + 2\sqrt{10 \cdot 106} = 116 + 2\sqrt{1060} = 116 + 4\sqrt{265}$.
Warunek $k>0$ jest spełniony.

Wartości parametru $k$, dla których okręgi są styczne, to $k=116 - 4\sqrt{265}$ lub $k=116 + 4\sqrt{265}$.

Odpowiedź: $k \in \{116 - 4\sqrt{265}, 116 + 4\sqrt{265}\}$.

**Grupa C**

1.  Okrąg 1: $x^2+(y+4)^2=36$
    Środek $S_1 = (0, -4)$, promień $r_1 = \sqrt{36} = 6$.

    Okrąg 2: $(x-8)^2+(y-2)^2=25$
    Środek $S_2 = (8, 2)$, promień $r_2 = \sqrt{25} = 5$.

Odległość między środkami okręgów:

$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$

$d = \sqrt{(8-0)^2 + (2-(-4))^2} = \sqrt{8^2 + (2+4)^2} = \sqrt{64 + 6^2} = \sqrt{64+36} = \sqrt{100} = 10$.

Suma promieni: $r_1 + r_2 = 6 + 5 = 11$.

Wartość bezwzględna różnicy promieni: $|r_1 - r_2| = |6 - 5| = 1$.

Porównanie $d$ z $r_1+r_2$ i $|r_1-r_2|$:

$d = 10$

$r_1+r_2 = 11$

$|r_1-r_2| = 1$

Ponieważ $|r_1-r_2| < d < r_1+r_2$ (czyli $1 < 10 < 11$), okręgi przecinają się w dwóch punktach.

Odpowiedź: C. 2

2.  Okrąg o środku $A(-1,-3)$ przechodzący przez $P(-2,4)$:
    
    Promień $r_A = \sqrt{(-2 - (-1))^2 + (4 - (-3))^2} = \sqrt{(-2+1)^2 + (4+3)^2} = \sqrt{(-1)^2 + 7^2} = \sqrt{1+49} = \sqrt{50}$.
    
    Równanie okręgu 1: $(x - (-1))^2 + (y - (-3))^2 = (\sqrt{50})^2 \Rightarrow (x+1)^2 + (y+3)^2 = 50$.

Okrąg o środku $B(-8,6)$ przechodzący przez $Q(-6,3)$:

Promień $r_B = \sqrt{(-6 - (-8))^2 + (3 - 6)^2} = \sqrt{(-6+8)^2 + (-3)^2} = \sqrt{2^2 + (-3)^2} = \sqrt{4+9} = \sqrt{13}$.

Równanie okręgu 2: $(x - (-8))^2 + (y - 6)^2 = (\sqrt{13})^2 \Rightarrow (x+8)^2 + (y-6)^2 = 13$.

Wzajemne położenie okręgów:

Środki: $S_A = (-1,-3)$, $S_B = (-8,6)$.

Promienie: $r_A = \sqrt{50}$, $r_B = \sqrt{13}$.

Odległość między środkami:

$d(A,B) = \sqrt{(-8 - (-1))^2 + (6 - (-3))^2} = \sqrt{(-7)^2 + 9^2} = \sqrt{49+81} = \sqrt{130}$.

Suma promieni: $r_A + r_B = \sqrt{50} + \sqrt{13}$.

Wartość bezwzględna różnicy promieni: $|r_A - r_B| = |\sqrt{50} - \sqrt{13}|$.

$(\sqrt{50} + \sqrt{13})^2 = 50 + 13 + 2\sqrt{50 \cdot 13} = 63 + 2\sqrt{650}$.

$d(A,B)^2 = (\sqrt{130})^2 = 130$.

Porównujemy $d(A,B)$ z $r_A+r_B$:

$130$ vs $63 + 2\sqrt{650}$.

$130 - 63$ vs $2\sqrt{650}$.

$67$ vs $2\sqrt{650}$.

Obie strony są dodatnie, podnosimy do kwadratu:

$67^2 = 4489$.

$(2\sqrt{650})^2 = 4 \cdot 650 = 2600$.

Ponieważ $4489 > 2600$, to $67 > 2\sqrt{650}$.

Zatem $d(A,B) > r_A+r_B$.

Okręgi są rozłączne zewnętrznie.

Równania okręgów: $(x+1)^2 + (y+3)^2 = 50$ i $(x+8)^2 + (y-6)^2 = 13$.

Wzajemne położenie: Okręgi są rozłączne zewnętrznie.

3.  Promienie okręgów: $r_1 = 9$, $r_2 = 3$.
    
    Okręgi są zewnętrznie styczne, więc odległość między ich środkami jest równa sumie ich promieni.
    
    $d = r_1 + r_2 = 9 + 3 = 12$.

Odpowiedź: D. 12

4. Promienie okręgów: $r_1 = 6$, $r_2 = 9$.
   
   Aby okręgi były rozłączne, odległość $d$ między ich środkami musi spełniać jeden z warunków:
1. Rozłączne zewnętrznie: $d > r_1 + r_2$.
   
   $d > 6 + 9 \Rightarrow d > 15$.
1. Rozłączne wewnętrznie (jeden okrąg wewnątrz drugiego, bez punktów wspólnych): $d < |r_1 - r_2|$.
   
   $d < |6 - 9| \Rightarrow d < |-3| \Rightarrow d < 3$.
   
   Ponieważ odległość $d$ musi być nieujemna ($d \ge 0$), warunek to $0 \le d < 3$.

Zatem okręgi są rozłączne, gdy $d > 15$ lub $0 \le d < 3$.

Odpowiedź: Odległość $d$ musi spełniać warunek $d > 15$ lub $0 \le d < 3$.

5.  Okrąg $O_1: x^2+y^2-6 x-4 y=0$.
    
    Przekształcamy do postaci kanonicznej:
    
    $(x^2-6x) + (y^2-4y) = 0$
    
    $(x^2-6x+9) - 9 + (y^2-4y+4) - 4 = 0$
    
    $(x-3)^2 + (y-2)^2 = 13$.
    
    Środek $S_1 = (3,2)$, promień $r_1 = \sqrt{13}$.

Okrąg $O_2: x^2+y^2+12 x-16 y+100-k=0$.

Przekształcamy do postaci kanonicznej:

$(x^2+12x) + (y^2-16y) = k-100$

$(x^2+12x+36) - 36 + (y^2-16y+64) - 64 = k-100$

$(x+6)^2 + (y-8)^2 = k-100+36+64$

$(x+6)^2 + (y-8)^2 = k$.

Środek $S_2 = (-6,8)$, promień $r_2 = \sqrt{k}$.

Aby $O_2$ był okręgiem, musi zachodzić $k>0$.

Odległość między środkami $S_1$ i $S_2$:

$d = \sqrt{(-6-3)^2 + (8-2)^2} = \sqrt{(-9)^2 + 6^2} = \sqrt{81+36} = \sqrt{117} = \sqrt{9 \cdot 13} = 3\sqrt{13}$.

Okręgi są styczne, jeśli $d = r_1+r_2$ (styczne zewnętrznie) lub $d = |r_1-r_2|$ (styczne wewnętrznie).

Przypadek 1: Styczne zewnętrznie ($d = r_1+r_2$)

$3\sqrt{13} = \sqrt{13} + \sqrt{k}$

$2\sqrt{13} = \sqrt{k}$

Podnosząc do kwadratu: $k = (2\sqrt{13})^2 = 4 \cdot 13 = 52$.

Warunek $k>0$ jest spełniony ($52>0$).

Przypadek 2: Styczne wewnętrznie ($d = |r_1-r_2|$)

$3\sqrt{13} = |\sqrt{13} - \sqrt{k}|$.

To równanie rozbijamy na dwa przypadki:

a) $\sqrt{13} - \sqrt{k} = 3\sqrt{13}$

$-\sqrt{k} = 2\sqrt{13}$

$\sqrt{k} = -2\sqrt{13}$. To równanie nie ma rozwiązania, ponieważ $\sqrt{k} \ge 0$.

b) $\sqrt{13} - \sqrt{k} = -3\sqrt{13}$

$-\sqrt{k} = -4\sqrt{13}$

$\sqrt{k} = 4\sqrt{13}$.

Podnosząc do kwadratu: $k = (4\sqrt{13})^2 = 16 \cdot 13 = 208$.

Warunek $k>0$ jest spełniony ($208>0$).

Wartości parametru $k$, dla których okręgi są styczne, to $k=52$ lub $k=208$.

Odpowiedź: $k \in \{52, 208\}$.
