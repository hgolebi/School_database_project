ALTER SESSION SET NLS_DATE_FORMAT = "DD/MM/YYYY";

-- test procedury zmiana_klasy
exec zmiana_klasy(7, 2);

-- test procedury nowy_dyrektor 
exec nowy_dyrektor (5);

/

-- test procedury nowy_dyrektor (równie¿ test triggera)
ALTER TRIGGER tr_czy_moze_byc_dyrektorem ENABLE;

INSERT INTO Nauczyciele VALUES (25, 'Krzysztof', 'Drzewicki', '12/07/2014');

exec nowy_dyrektor (25);

-- test funkcji ile_lat_pracuje
SELECT ile_lat_pracuje(20) from dual;

-- test funkcji srednia_z_przedmiotu

SELECT srednia_z_przedmiotu(1, 2) from dual;

-- czy uczen, ktoremu zostala przypisana ocena do przedmiotu, chodzi na ten przedmiot (test_triggera)
ALTER TRIGGER tr_czy_uczen_chodzi_na_przedmiot ENABLE;

UPDATE Oceny_uczniow
SET ocena_id = 4, konkretny_przedmiot_id = 2 
WHERE uczen_id = 1;


-- zapytanie, zwracajace ilu uczniow chodzi do danej klasy
SELECT klasa_id, COUNT(uczen_id)
FROM uczniowie
GROUP BY klasa_id
ORDER BY klasa_id asc;