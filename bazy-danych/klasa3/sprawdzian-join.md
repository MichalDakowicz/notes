[Wstecz](../bazy-danych.md)

# Sprawdzian JOIN

**Łączenie tabel (JOIN)**

-   **`INNER JOIN`**: Zwraca tylko pasujące wiersze z obu tabel, na podstawie warunku złączenia.
-   **`LEFT JOIN`**: Zwraca wszystkie wiersze z lewej tabeli i pasujące wiersze z prawej tabeli. Jeśli nie ma pasującego wiersza w prawej tabeli, zwraca `NULL`.
-   **`RIGHT JOIN`**: Zwraca wszystkie wiersze z prawej tabeli i pasujące wiersze z lewej tabeli. Jeśli nie ma pasującego wiersza w lewej tabeli, zwraca `NULL`.
-   **`FULL JOIN` (symulacja w MySQL)**: Łączy wyniki `LEFT JOIN` i `RIGHT JOIN` za pomocą `UNION`, zwracając wszystkie wiersze z obu tabel.

**Przykład:**

```sql
-- Pobieranie danych klientów i ich zamówień (wszyscy klienci, nawet bez zamówień)
SELECT klienci.*, zamowienia.id_zamowienia
FROM klienci
LEFT JOIN zamowienia ON klienci.id_klienta = zamowienia.id_klienta;
```

**Samozłączenie (SELF JOIN)**

-   Używane do łączenia tabeli samej ze sobą, tak jakby były to dwie oddzielne tabele. Przydatne do porównywania wierszy w tej samej tabeli.

**Przykład:**

```sql
-- Pobieranie danych klientów z tego samego miasta
SELECT k1.*
FROM klienci k1
INNER JOIN klienci k2 ON k1.miasto = k2.miasto AND k1.id_klienta <> k2.id_klienta
ORDER BY k1.miasto;
```

**Funkcje agregujące**

-   `COUNT(*)`: Liczy wszystkie wiersze w grupie lub tabeli.
-   `COUNT(kolumna)`: Liczy nie-NULLowe wartości w określonej kolumnie.
-   `SUM(kolumna)`: Sumuje wartości w określonej kolumnie.
-   `AVG(kolumna)`: Oblicza średnią wartość w określonej kolumnie.
-   `MIN(kolumna)`: Znajduje minimalną wartość w określonej kolumnie.
-   `MAX(kolumna)`: Znajduje maksymalną wartość w określonej kolumnie.

**Przykład:**

```sql
-- Oblicza średnią cenę produktów
SELECT AVG(cena_jednostkowa) AS srednia_cena
FROM produkty;
```

**Grupowanie (GROUP BY)**

-   Grupuje wiersze na podstawie wartości w określonych kolumnach. Używane z funkcjami agregującymi do obliczania wartości dla każdej grupy.

**Przykład:**

```sql
-- Liczy liczbę klientów w każdym kraju
SELECT kraj, COUNT(*) AS liczba_klientow
FROM klienci
GROUP BY kraj;
```

**Filtrowanie grup (HAVING)**

-   Filtruje grupy utworzone przez `GROUP BY` na podstawie warunku.

**Przykład:**

```sql
-- Pobiera kraje z więcej niż dwoma klientami
SELECT kraj, COUNT(*) AS liczba_klientow
FROM klienci
GROUP BY kraj
HAVING COUNT(*) > 2;
```

Pamiętaj, że to tylko podstawowe informacje. Przed sprawdzianem warto przećwiczyć różne kombinacje tych poleceń i upewnić się, że rozumiesz, jak działają. Powodzenia!
