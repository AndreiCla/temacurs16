import csv
import pandas as pd
CALE_FISIER = "/Users/bindarclaudiu-andrei/Documents/K/Teme/Temacurs16/ListaAngajati.csv"
# col = ['Nume', 'Prenume', 'Plata']
# name = "ListaAngajati.csv"

# with open(name, 'w') as csvfile:
#     cswriter = csv.writer(csvfile)
#     cswriter.writerow(col)


def adaugareAngajat():
    content = pd.read_csv(CALE_FISIER)
    nume = input("Nume angajat: ")
    prenume = input("Prenume angajat: ")
    plata = input("Salariul angajatului: ")

    content.loc[len(content.index)] = [nume, prenume, plata]

    content.to_csv(CALE_FISIER, index=False)


adaugareAngajat()

