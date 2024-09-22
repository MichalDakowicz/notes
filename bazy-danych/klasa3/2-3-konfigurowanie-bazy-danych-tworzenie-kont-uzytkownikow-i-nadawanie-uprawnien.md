[Wstecz](../bazy-danych.md)

# 2-3 Konfigurowanie bazy danych. Tworzenie kont użytkowników i nadawanie uprawnień.

1. Użyj pakietu XAMPP (https://www.apachefriends.org/).
   W jego skład wchodzi:

-   baza MySQL (MariaDB),
-   narzędzie administracyjne phpMyAdmin.

2. Aby uzyskać dostęp do phpMyAdmin uruchom panel sterowania XAMPP oraz uruchom serwer Apache i MySQL. Następnie w oknie przeglądarki wpisz http://localhost/phpMyAdmin (lub http://127.0.0.1/phpmyadmin)

3. Utwórz nową bazę danych Imie_Nazwisko

```sql
CREATE DATABASE Michal_Dakowicz;
```

4. W bazie danych Imie_Nazwisko utwórz tabele

```sql
CREATE TABLE Uczniowie(
    Id_Ucznia INT AUTO_INCREMENT PRIMARY KEY,
    Nazwisko VARCHAR(40),
    Imie VARCHAR(25),
    Ulica VARCHAR(25)
);
CREATE TABLE TelefonyUczniow(
    Id_Ucznia INT,
    Telefon INT,
    PRIMARY KEY(Id_Ucznia, Telefon)
);
```

5. Utwórz nowe konto użytkownika o nazwie zgodnej z pierwszymi literami własnego imienia i nazwiska (np. IN)

```sql
CREATE USER 'MD'@'localhost' IDENTIFIED BY 'MD';
```

6. Zmień hasło użytkownikowi IN

```sql
SET PASSWORD FOR 'MD'@'localhost' = PASSWORD('MD');
```

7. Zmień nazwę użytkownika na I_N

```sql
RENAME USER 'MD'@'localhost' TO 'M_D'@'localhost';
```

8. Usuń użytkownika I_N

```sql
DROP USER 'M_D'@'localhost';
```

9. Utwórz nowe konto użytkownika o nazwie zgodnej z własnym imieniem i nazwiskiem

```sql
CREATE USER 'MichalDakowicz'@'localhost' IDENTIFIED BY 'MichalDakowicz';
```

10. Wstaw znak podkreślenia pomiędzy imieniem i nazwiskiem

```sql
RENAME USER 'MichalDakowicz'@'localhost' TO 'Michal_Dakowicz'@'localhost';
```

11. Zmień hasło na dziesięcioznakowe z przynajmniej jedną dużą literą, znakiem specjalnym i cyfrą

```sql
SET PASSWORD FOR 'Michal_Dakowicz'@'localhost' = PASSWORD('MichalDakowicz1!');
```

12. Sprawdź uprawnienia nowego użytkownika

```sql
SHOW GRANTS FOR 'Michal_Dakowicz'@'localhost';
```

13. Użytkownikowi o nazwie zgodnej z własnym imieniem i nazwiskiem nadaj uprawnienie do wyszukiwania danych we wszystkich tabelach bazy danych Imie_Nazwisko

```sql
GRANT SELECT ON Imie_Nazwisko.* TO 'Michal_Dakowicz'@'localhost';
```

14. Sprawdź czy użytkownik może korzystać z tego uprawnienia

```sql
SHOW GRANTS FOR 'Michal_Dakowicz'@'localhost';
```

15. Użytkownikowi o nazwie zgodnej z własnym imieniem i nazwiskiem nadaj uprawnienie do wstawiania danych do tabeli uczniowie w bazie danych Imie_Nazwisko

```sql
GRANT INSERT ON Michal_Dakowicz.Uczniowie TO 'Michal_Dakowicz'@'localhost';
```

16. Sprawdź czy użytkownik może korzystać z tego uprawnienia

```sql
SHOW GRANTS FOR 'Michal_Dakowicz'@'localhost';
```

17. Użytkownikowi o nazwie zgodnej z własnym imieniem i nazwiskiem nadaj uprawnienie do usuwania i modyfikowania danych z tabeli telefony uczniów w bazie danych Imie_Nazwisko

```sql
GRANT DELETE, UPDATE ON Michal_Dakowicz.TelefonyUczniow TO 'Michal_Dakowicz'@'localhost';
```

18. Sprawdź czy użytkownik może korzystać z tych uprawnień

```sql
SHOW GRANTS FOR 'Michal_Dakowicz'@'localhost';
```

19. Użytkownikowi o nazwie zgodnej z własnym imieniem i nazwiskiem nadaj uprawnienie do tworzenia nowych tabel w bazie danych Imie_Nazwisko

```sql
GRANT CREATE ON Imie_Nazwisko.* TO 'Michal_Dakowicz'@'localhost';
```

20. Sprawdź czy użytkownik może korzystać z tego uprawnienia

```sql
SHOW GRANTS FOR 'Michal_Dakowicz'@'localhost';
```

21. Sprawdź uprawnienia nowego użytkownika

```sql
CREATE USER 'NowyUzytkownik'@'localhost' IDENTIFIED BY 'NowyUzytkownik';

SHOW GRANTS FOR 'NowyUzytkownik'@'localhost';
```

22. Zabierz uprawnienie do usuwania danych

```sql
REVOKE DELETE ON Michal_Dakowicz.TelefonyUczniow FROM 'Michal_Dakowicz'@'localhost';
```
