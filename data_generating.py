from random import choice, randrange, seed


names = ['Piotr', 'Jakub', 'Marian', 'Hubert', 'Wojciech', 'Marcin', 'Tomasz', 'Bartosz', 'Bartlomiej']
surnames = ['Go', 'To', 'Bi', 'Ro', 'Ru', 'Mu', 'Mo', 'Ko', 'Drze', 'Krze', 'Odrze', 'Prze']
surnames2= ['wecki', 'wacki', 'wicki']
Przedmioty = ['matematyka', 'jezyk polski', 'jezyk angielski', 'biologia', 'chemia', 'historia']

# NAUCZYCIELE
def nauczyciele():
    for i in range (24):
        seed(randrange(1,1000))
        text = 'INSERT INTO Nauczyciele VALUES '
        id = 1 + i
        name = choice(names)
        surname = choice(surnames) + choice(surnames2)
        dd = randrange(10, 28)
        mm = randrange(1, 9)
        rr = randrange(1970, 2005)

        text += f'({id}, \'{name}\', \'{surname}\', \'{dd}/0{mm}/{rr}\');\n'

        file = open("Wstawianie_danych.sql", 'a')
        file.write(text)
    file.write("-----------\n")
    file.close

#KLASY
def klasy():

    id = 0
    num = 0
    for i in range(3):

        num += 1
        let = ord('A') - 1
        for j in range(4):
            text = 'INSERT INTO Klasy VALUES '
            id += 1
            let += 1
            text += f'({id}, {num}, \'{chr(let)}\', {id+4});\n'
            file = open("Wstawianie_danych.sql", 'a')
            file.write(text)
    file.write("-----------\n")
    file.close



# UCZNIOWIE
def uczniowie():
    id = 0
    for kl in range (12):
        for i in range (15):
            seed(randrange(1, 1000))
            text = 'INSERT INTO Uczniowie VALUES '
            id += 1
            name = choice(names)
            surname = choice(surnames) + choice(surnames2)
            text += f'({id}, \'{name}\', \'{surname}\', {kl+1});\n'
            file = open("Wstawianie_danych.sql", 'a')
            file.write(text)
    file.write("-----------\n")
    file.close

def przedmioty():

    id = 0
    for p in Przedmioty:
        text = 'INSERT INTO Przedmioty VALUES '
        id += 1
        text += f'({id}, \'{p}\');\n'
        file = open("Wstawianie_danych.sql", 'a')
        file.write(text)
    file.write("-----------\n")
    file.close

def konkretne_przedmioty():
    id = 0
    n_id = 0
    p_id = 0
    for p in Przedmioty:
        p_id += 1
        kl_id = 0
        for i in range(4):
            n_id += 1
            for j in range(3):
                kl_id += 1
                id += 1
                text = 'INSERT INTO Konkretne_przedmioty VALUES '
                text += f'({id}, {p_id}, {kl_id}, {n_id});\n'
                file = open("Wstawianie_danych.sql", 'a')
                file.write(text)
    file.write("-----------\n")
    file.close

def oceny():
    oceny = ['niedostateczna', 'dopuszczjaca', "dostateczna", 'dobra', "bardzo dobra", 'celujaca']
    for i in range(6):
        id = i + 1
        name = oceny[i]
        text = 'INSERT INTO Oceny VALUES '
        text += f'({id}, {id}, \'{name}\');\n'
        file = open("Wstawianie_danych.sql", 'a')
        file.write(text)
    file.write("-----------\n")
    file.close

def oceny_uczniow():
    id = 24
    for kl in range (12):
        for u in range (15):
            id += 1
            u_id = kl*15 + u + 1
            p_id = randrange(kl*6+1, kl*6+6)
            oc = randrange(1, 6)
            dd = randrange(10, 30)
            mm = randrange(10, 12)
            rr = 2022
            text = 'INSERT INTO Oceny_uczniow VALUES '
            text += f'({id}, {u_id}, {oc}, \'{dd}/{mm}/{rr}\', {p_id}, null);\n'
            file = open("Wstawianie_danych.sql", 'a')
            file.write(text)
    file.write("-----------\n")
    file.close

file = open("Wstawianie_danych.sql", 'a')
file.write("ALTER SESSION SET NLS_DATE_FORMAT = \"DD/MM/YYYY\";\n")
file.write("-----------\n")

oceny()
nauczyciele()
przedmioty()
klasy()
uczniowie()
konkretne_przedmioty()
oceny_uczniow()




