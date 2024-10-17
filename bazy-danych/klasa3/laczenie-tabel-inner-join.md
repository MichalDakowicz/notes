[Wstecz](../bazy-danych.md)

# 4 Łączenie tabel - INNER JOIN

**Baza danych [NorthWind](northwind.sql)**

**1. Zaimportuj bazę danych NorthWind**

```sql
CREATE DATABASE northwind;
```

Importuj plik **northwind.sql** do bazy danych northwind w [_phpMyAdmin_](http://127.0.0.1/phpmyadmin)

**2. Podaj numer zamówienia oraz nazwę klienta**

```sql
SELECT zamowienia.id_zamowienia, klienci.nazwa_firmy FROM zamowienia
INNER JOIN klienci ON zamowienia.id_klienta = klienci.id_klienta;
```

**3. Wybierz tylko klientów z Białegostoku**

```sql
SELECT * FROM klienci WHERE miasto = 'Białystok';
```

**4. Podaj nazwy produktów i ich kategorie**

```sql
SELECT produkty.nazwa, kategorie.nazwa FROM produkty
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria;
```

**5. Wybierz tylko produkty kategorii spożywcze**

```sql
SELECT produkty.nazwa, kategorie.nazwa FROM produkty
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria
WHERE kategorie.nazwa = 'spożywcze';
```

**6. Podaj wszystkie numery zamówień z informacjami o nazwie klienta i nadawcy**

```sql
SELECT zamowienia.id_zamowienia, klienci.nazwa_firmy, pracownicy.imie, pracownicy.nazwisko FROM zamowienia
INNER JOIN klienci ON zamowienia.id_klienta = klienci.id_klienta
INNER JOIN pracownicy ON zamowienia.id_pracownika = pracownicy.id_pracownik;
```

**7. Podać nazwy dostawców produktów kategorii elektronika**

```sql
SELECT DISTINCT dostawcy.nazwa_firmy FROM dostawcy
INNER JOIN produkty ON dostawcy.id_dostwcy = produkty.id_dostwcy
WHERE produkty.id_kategoria IN (4, 5, 6);
```

**8. Podaj numery zamówień, nazwy klientów, nazwiska pracowników obsługujących zamówienie i daty zamówień**

```sql
SELECT zamowienia.id_zamowienia, klienci.nazwa_firmy, pracownicy.nazwisko, zamowienia.data_zamowienia FROM zamowienia
INNER JOIN klienci ON zamowienia.id_klienta = klienci.id_klienta
INNER JOIN pracownicy ON zamowienia.id_pracownika = pracownicy.id_pracownik;
```

**9. Podaj numery zamówień, nazwy klientów, nazwiska pracowników obsługujących zamówienie z kwietnia 2021 roku**

```sql
SELECT zamowienia.id_zamowienia, klienci.nazwa_firmy, pracownicy.nazwisko, zamowienia.data_zamowienia FROM zamowienia
INNER JOIN klienci ON zamowienia.id_klienta = klienci.id_klienta
INNER JOIN pracownicy ON zamowienia.id_pracownika = pracownicy.id_pracownik
WHERE data_zamowienia BETWEEN '2021-04-01' AND '2021-04-30';
```

**10. Podaj numery zamówień, nazwy produktów i kategorii, nazwy spedytorów obsługujących zamówienie i kraj odbiorcy**

```sql
SELECT zamowienia.id_zamowienia, produkty.nazwa, kategorie.nazwa, spedytorzy.nazwa, zamowienia.kraj_odbiorcy FROM zamowienia
INNER JOIN szczegoly_zamowien ON zamowienia.id_zamowienia = szczegoly_zamowien.id_zamowienia
INNER JOIN produkty ON szczegoly_zamowien.id_produkt = produkty.id_produkt
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria
INNER JOIN spedytorzy ON zamowienia.id_spedytora = spedytorzy.id_spedytora;
```
