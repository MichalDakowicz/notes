[Wstecz](../bazy-danych.md)

# 5 Łączenie tabel - LEFT JOIN, RIGHT JOIN

**1. Podaj dane wszystkich klientów i numery ich zamówień.**

```sql
SELECT klienci.*, zamowienia.id_zamowienia
FROM klienci
LEFT JOIN zamowienia ON klienci.id_klienta = zamowienia.id_klienta;
```

**2. Sprawdź różnicę w wynikach zapytań z INNER JOIN i LEFT JOIN**

```sql
-- INNER JOIN (zwraca tylko klientów, którzy złożyli zamówienia)
SELECT klienci.*, zamowienia.id_zamowienia
FROM klienci
INNER JOIN zamowienia ON klienci.id_klienta = zamowienia.id_klienta;

-- LEFT JOIN (zwraca wszystkich klientów, nawet jeśli nie złożyli zamówienia)
SELECT klienci.*, zamowienia.id_zamowienia
FROM klienci
LEFT JOIN zamowienia ON klienci.id_klienta = zamowienia.id_klienta;
```

**3. Podaj dane klientów, którzy nie złożyli zamówień**

```sql
SELECT klienci.*
FROM klienci
LEFT JOIN zamowienia ON klienci.id_klienta = zamowienia.id_klienta
WHERE zamowienia.id_zamowienia IS NULL;
```

**4. Podaj nazwy wszystkich produktów i ich kategorie**

```sql
-- INNER JOIN (zwraca produkty mające przypisaną kategorię)
SELECT produkty.nazwa AS nazwa_produktu, kategorie.nazwa AS nazwa_kategorii
FROM produkty
INNER JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria;

-- LEFT JOIN (zwraca wszystkie produkty, nawet bez przypisanej kategorii)
SELECT produkty.nazwa AS nazwa_produktu, kategorie.nazwa AS nazwa_kategorii
FROM produkty
LEFT JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria;
```

**5. Wybierz wszystkie kategorie i produkty tych kategorii**

```sql
SELECT kategorie.nazwa AS nazwa_kategorii, produkty.nazwa AS nazwa_produktu
FROM kategorie
LEFT JOIN produkty ON kategorie.id_kategoria = produkty.id_kategoria;
```

**6. Zwróć dane wszystkich pracowników i obsługiwane przez nich zamówienia. Użyj RIGHT JOIN**

```sql
SELECT pracownicy.*, zamowienia.id_zamowienia
FROM zamowienia
RIGHT JOIN pracownicy ON zamowienia.id_pracownika = pracownicy.id_pracownik;
```

**7. Podaj dane pracowników nie obsługujących zamówień**

```sql
SELECT pracownicy.*
FROM pracownicy
LEFT JOIN zamowienia ON pracownicy.id_pracownik = zamowienia.id_pracownika
WHERE zamowienia.id_zamowienia IS NULL;
```

**8. Na tabelach pracownicy i zamówienia sprawdź różnicę w wynikach zapytań z LEFT JOIN i RIGHT JOIN**

```sql
-- LEFT JOIN (wszyscy pracownicy, nawet jeśli nie obsługiwali zamówień)
SELECT pracownicy.*, zamowienia.id_zamowienia
FROM pracownicy
LEFT JOIN zamowienia ON pracownicy.id_pracownika = zamowienia.id_pracownika;

-- RIGHT JOIN (wszystkie zamówienia, nawet jeśli nie mają przypisanego pracownika)
SELECT pracownicy.*, zamowienia.id_zamowienia
FROM pracownicy
RIGHT JOIN zamowienia ON pracownicy.id_pracownika = zamowienia.id_pracownika;
```

**9. Podaj wszystkie numery zamówień z informacjami o nazwie klienta i spedytora**

```sql
SELECT zamowienia.id_zamowienia, klienci.nazwa_firmy AS nazwa_klienta, spedytorzy.nazwa AS nazwa_spedytora
FROM zamowienia
LEFT JOIN klienci ON zamowienia.id_klienta = klienci.id_klienta
LEFT JOIN spedytorzy ON zamowienia.id_spedytora = spedytorzy.id_spedytora;
```

**10. Podaj nazwiska klientów, numery zamówień, nazwiska pracowników obsługujących zamówienia i daty zamówień**

```sql
SELECT klienci.nazwisko AS nazwisko_klienta,
       zamowienia.id_zamowienia,
       pracownicy.nazwisko AS nazwisko_pracownika,
       zamowienia.data_zamowienia
FROM zamowienia
LEFT JOIN klienci ON zamowienia.id_klienta = klienci.id_klienta
LEFT JOIN pracownicy ON zamowienia.id_pracownika = pracownicy.id_pracownik;
```
