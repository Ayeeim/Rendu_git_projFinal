import random

#Variable globale:
data = []
#Récupère la liste des mots dans donnees.txt
file = "data.txt"
with open(file) as dataFile:
    data = [line.strip() for line in dataFile.readlines()]

#Récupère un mot aléatoirement dans les données
def pick_random_word(data):
    i = random.randint(0,len(data)-1)
    return data.pop(i)
