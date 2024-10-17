[Wstecz](../bazy-danych.md)

# 6 Łączenie tabel - FULL JOIN, SELF JOIN

**MySQL nie obsługuje FULL JOIN, więc musisz łączyć LEFT JOIN i RIGHT JOIN**

**1. Podaj dane wszystkich klientów i wszystkie numery zamówień**

```sql
SELECT klienci.imie, klienci.nazwisko, zamowienia.id_zamowienia
FROM klienci
LEFT JOIN zamowienia ON klienci.id_klienta = zamowienia.id_klienta
UNION
SELECT klienci.imie, klienci.nazwisko, zamowienia.id_zamowienia
FROM zamowienia
RIGHT JOIN klienci ON klienci.id_klienta = zamowienia.id_klienta;
```

**2. Sprawdź różnicę w wynikach zapytań z INNER JOIN, LEFT JOIN, RIGHT JOIN i FULL JOIN na podstawie zadania 1**

| Typ złączenia | Opis                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------- |
| `INNER JOIN`  | Zwróci tylko klientów, którzy złożyli zamówienie i zamówienia, które mają przypisanego klienta.   |
| `LEFT JOIN`   | Zwróci wszystkich klientów i ich zamówienia (jeśli istnieją).                                     |
| `RIGHT JOIN`  | Zwróci wszystkie zamówienia i klientów, którzy je złożyli (jeśli istnieją).                       |
| `FULL JOIN`   | Zwróci wszystkich klientów i wszystkie zamówienia, niezależnie od tego, czy są ze sobą połączone. |

**3. Czy są złożone zamówienia bez określonego klienta**

```sql
SELECT *
FROM zamowienia
LEFT JOIN klienci ON zamowienia.id_klienta = klienci.id_klienta
WHERE klienci.id_klienta IS NULL;
```

**4. Podaj nazwy wszystkich produktów i wszystkich kategorii**

```sql
SELECT produkty.nazwa, kategorie.nazwa
FROM produkty
LEFT JOIN kategorie ON produkty.id_kategoria = kategorie.id_kategoria
UNION
SELECT produkty.nazwa, kategorie.nazwa
FROM kategorie
RIGHT JOIN produkty ON produkty.id_kategoria = kategorie.id_kategoria;
```

**5. Wybierz wszystkich pracowników i wszystkie oddziały**

```sql
SELECT pracownicy.*, oddzial.nazwa
FROM pracownicy
LEFT JOIN oddzial ON pracownicy.id_odzial = oddzial.id_odzial
UNION
SELECT pracownicy.*, oddzial.nazwa
FROM oddzial
RIGHT JOIN pracownicy ON pracownicy.id_odzial = oddzial.id_odzial;
```

**6. Podaj dane klientów z tego samego miasta, uporządkuj wg miasta**

```sql
SELECT k1.imie, k1.nazwisko
FROM klienci k1
INNER JOIN klienci k2 ON k1.miasto = k2.miasto AND k1.id_klienta <> k2.id_klienta
ORDER BY k1.miasto;
```

**7. Podaj dane pracowników z tego samego oddziału, uporządkuj wg oddziału**

```sql
SELECT p1.imie, p1.nazwisko
FROM pracownicy p1
INNER JOIN pracownicy p2 ON p1.id_odzial = p2.id_odzial AND p1.id_pracownik <> p2.id_pracownik
ORDER BY p1.id_odzial;
```

**8. Na tabeli dostawcy sprawdź samozłączenie w WHERE i z INNER JOIN podając dostawców z tego samego kraju. Wynik uporządkuj wg miasta**

**Samozłączenie w WHERE:**

```sql
SELECT d1.*
FROM dostawcy d1, dostawcy d2
WHERE d1.kraj = d2.kraj AND d1.id_dostwcy <> d2.id_dostwcy
ORDER BY d1.miasto;
```

**Samozłączenie z INNER JOIN:**

```sql
SELECT d1.*
FROM dostawcy d1
INNER JOIN dostawcy d2 ON d1.kraj = d2.kraj AND d1.id_dostwcy <> d2.id_dostwcy
ORDER BY d1.miasto;
```

**9. Na tabelach pracownicy i zamówienia sprawdź różnicę w wynikach zapytań z INNER JOIN, LEFT JOIN, RIGHT JOIN i FULL JOIN**

```sql
-- INNER JOIN (tylko pracownicy z przypisanymi zamówieniami i vice versa)
SELECT p.*, z.id_zamowienia
FROM pracownicy p
INNER JOIN zamowienia z ON p.id_pracownika = z.id_pracownika;

-- LEFT JOIN (wszyscy pracownicy, nawet bez przypisanych zamówień)
SELECT p.*, z.id_zamowienia
FROM pracownicy p
LEFT JOIN zamowienia z ON p.id_pracownika = z.id_pracownika;

-- RIGHT JOIN (wszystkie zamówienia, nawet bez przypisanych pracowników)
SELECT p.*, z.id_zamowienia
FROM pracownicy p
RIGHT JOIN zamowienia z ON p.id_pracownika = z.id_pracownika;

-- FULL JOIN (wszyscy pracownicy i wszystkie zamówienia)
SELECT p.*, z.id_zamowienia
FROM pracownicy p
LEFT JOIN zamowienia z ON p.id_pracownika = z.id_pracownika
UNION
SELECT p.*, z.id_zamowienia
FROM zamowienia z
RIGHT JOIN pracownicy p ON p.id_pracownika = z.id_pracownika;
```
