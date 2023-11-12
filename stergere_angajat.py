import pandas as pd
import csv

def removeRowsWithValue(inputFile, outputFile, value):
    content = pd.read_csv(inputFile)
    content = content.loc[content["Nume"] != value]
    content.shape
    content.to_csv(outputFile, index=False)

removeRowsWithValue("/Users/bindarclaudiu-andrei/Documents/K/Teme/Temacurs16/ListaAngajati.csv","/Users/bindarclaudiu-andrei/Documents/K/Teme/Temacurs16/Lista2.csv","Vasile")