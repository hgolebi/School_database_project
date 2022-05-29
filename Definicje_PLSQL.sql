-- funkcja ktora bierze id nauczyciela i zwraca liczbe pelnych lat (365 dni), ktore dany nauczyciel juz przepracowal w tej szkole
CREATE OR REPLACE FUNCTION ile_lat_pracuje(n_id NUMBER)
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

-- trigger, ktory sprawdza czy dany nauczyciel moze byc dyrektorem (czy ma co najmniej 30 lat stazu)
CREATE OR REPLACE TRIGGER tr_czy_moze_byc_dyrektorem
BEFORE INSERT OR UPDATE ON Dyrektorowie FOR EACH ROW
DECLARE
    lata NUMBER;
BEGIN
    lata := ile_lat_pracuje(:old.nauczyciel_id);
    IF lata < 30 THEN
        raise_application_error(-20001, 'Dyrektor musi miec co najmniej 30 lat stazu');
    END IF;
END;
/
-- trigger, ktory sprawdza, czy uczen, ktoremu zostala przypisana ocena do przedmiotu, chodzi na ten przedmiot
CREATE OR REPLACE TRIGGER tr_czy_uczen_chodzi_na_przedmiot
BEFORE INSERT OR UPDATE ON Oceny_uczniow FOR EACH ROW
DECLARE
    kl_id NUMBER;
    czy_jest NUMBER;
BEGIN
    SELECT klasa_id INTO kl_id FROM Konkretne_przedmioty WHERE konkretny_przedmiot_id = :old.konkretny_przedmiot_id;
    SELECT COUNT(*) INTO czy_jest FROM Uczniowie WHERE uczen_id = :old.uczen_id AND klasa_id = kl_id;
    IF czy_jest = 0 THEN
        raise_application_error(-20002, 'Uczniowi zostala przypisana ocena z przedmiotu, na ktory nie chodzi');
    END IF;
END;