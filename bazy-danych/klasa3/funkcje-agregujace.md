[Wstecz](../bazy-danych.md)

# 7 Funkcje agregujące

**1. Podaj liczbę wszystkich klientów**

```sql
SELECT COUNT(*)
FROM klienci;
```

**2. Podaj liczbę klientów z Londynu**

```sql
SELECT COUNT(*)
FROM klienci
WHERE miasto = 'Londyn';
```

**3. Podaj liczbę pracowników na stanowisku sprzedawca**

```sql
SELECT COUNT(*)
FROM pracownicy
INNER JOIN oddzial ON pracownicy.id_odzial = oddzial.id_odzial
WHERE oddzial.nazwa = 'sprzedawca';
```

**4. Podaj liczbę typów kategorii produktów oraz liczbę dostawców produktów**

```sql
SELECT COUNT(DISTINCT id_kategoria),
       COUNT(DISTINCT id_dostwcy)
FROM produkty;
```

**5. Podaj sumaryczną liczbę zamówionych produktów**

```sql
SELECT SUM(ilosc)
FROM szczegoly_zamowien;
```

**6. Podaj sumaryczną liczbę zamówionych pralek**

```sql
SELECT SUM(szczegoly_zamowien.ilosc)
FROM szczegoly_zamowien
INNER JOIN produkty ON szczegoly_zamowien.id_produkt = produkty.id_produkt
WHERE produkty.nazwa = 'Pralka';
```

**7. Podaj cenę minimalną, maksymalną i średnią wszystkich produktów**

```sql
SELECT MIN(cena_jednostkowa),
       MAX(cena_jednostkowa),
       AVG(cena_jednostkowa)
FROM produkty;
```

**8. Podaj cenę minimalną, maksymalną i średnią produktów kategorii komputery**

```sql
SELECT MIN(produkty.cena_jednostkowa),
       MAX(produkty.cena_jednostkowa),
       AVG(produkty.cena_jednostkowa)
FROM produkty
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria
WHERE kategorie.nazwa = 'komputery';
```
