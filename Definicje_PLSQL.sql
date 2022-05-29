-- funkcja ktora bierze id nauczyciela i zwraca liczbe pelnych lat (365 dni), ktore dany nauczyciel juz przepracowal w tej szkole
CREATE OR REPLACE FUNCTION ile_lat_pracuje (n_id NUMBER)
RETURN NUMBER
AS
    lata NUMBER;
    dni NUMBER;
BEGIN
    SELECT FLOOR(SYSDATE - data_dolaczenia) INTO dni FROM Nauczyciele WHERE nauczyciel_id = n_id;
    lata := FLOOR (dni / 365);
    RETURN lata;
END;
/

    