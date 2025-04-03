import random

#Variable globale:
data = []
#Récupère la liste des mots dans donnees.txt
file = "data.txt"
with open(file) as dataFile:
    data = [line.strip() for line in dataFile.readlines()]

