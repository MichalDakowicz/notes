[Wstecz](../bazy-danych.md)

# 8 Grupowanie GROUP BY, Klauzula HAVING

**1. Podaj liczbę klientów z poszczególnych krajów**

```sql
SELECT kraj, COUNT(*) AS liczba_klientow
FROM klienci
GROUP BY kraj;
```

**2. Dla każdego id_produktu podaj sumaryczną ilość zamówionych produktów (tabela szczegoly_zamowien)**

```sql
SELECT id_produkt, SUM(ilosc) AS suma_zamowionych
FROM szczegoly_zamowien
GROUP BY id_produkt;
```

**3. Dla każdej id_kategoria podaj minimalną cenę jednostkową produktów**

```sql
SELECT id_kategoria, MIN(cena_jednostkowa) AS minimalna_cena
FROM produkty
GROUP BY id_kategoria;
```

**4. Dla każdej nazwy kategorii podaj minimalną cenę jednostkową produktów**

```sql
SELECT kategorie.nazwa AS nazwa_kategorii, MIN(produkty.cena_jednostkowa) AS minimalna_cena
FROM produkty
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria
GROUP BY kategorie.nazwa;
```

**5. Dla każdej nazwy oddziału podaj liczbę pracowników**

```sql
SELECT oddzial.nazwa AS nazwa_oddzialu, COUNT(*) AS liczba_pracownikow
FROM pracownicy
INNER JOIN oddzial ON pracownicy.id_odzial = oddzial.id_odzial
GROUP BY oddzial.nazwa;
```

**6. Podaj nazwy krajów z których jest powyżej 2 klientów**

```sql
SELECT kraj, COUNT(*) AS liczba_klientow
FROM klienci
GROUP BY kraj
HAVING COUNT(*) > 2;
```

**7. Podać nazwę kraju z którego jest tylko jeden pracownik**

```sql
SELECT kraj, COUNT(*) AS liczba_pracownikow
FROM pracownicy
GROUP BY kraj
HAVING COUNT(*) = 1;
```

**8. Podaj nazwy kategorii, których sumaryczne ceny produktów są powyżej 10000**

```sql
SELECT kategorie.nazwa AS nazwa_kategorii, SUM(produkty.cena_jednostkowa) AS suma_cen
FROM produkty
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria
GROUP BY kategorie.nazwa
HAVING SUM(produkty.cena_jednostkowa) > 10000;
```

**9. Podaj nazwy kategorii z minimalną cenę jednostkową produktów poniżej 20**

```sql
SELECT kategorie.nazwa AS nazwa_kategorii, MIN(produkty.cena_jednostkowa) AS minimalna_cena
FROM produkty
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria
GROUP BY kategorie.nazwa
HAVING MIN(produkty.cena_jednostkowa) < 20;
```

**10. Podaj nazwy oddziałów z liczbą pracowników z przedziału od 2 do 5**

```sql
SELECT oddzial.nazwa AS nazwa_oddzialu, COUNT(*) AS liczba_pracownikow
FROM pracownicy
INNER JOIN oddzial ON pracownicy.id_odzial = oddzial.id_odzial
GROUP BY oddzial.nazwa
HAVING COUNT(*) BETWEEN 2 AND 5;
```
