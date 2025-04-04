import random

#Variable globale:
data = []
charTested = []

#Récupère la liste des mots dans donnees.txt
file = "data.txt"
with open(file) as dataFile:
    data = [line.strip() for line in dataFile.readlines()]

#Récupère un mot aléatoirement dans les données
def pick_random_word(data):
    i = random.randint(0,len(data)-1)
    return data.pop(i)

#Tester si une lettre est déja utilisée:
def already_used(char):
    return (char in charTested)
#Demande à l'utilisateur de saisir une lettre:
def prop_letter():
    #Demander une lettre
    char = input("Quelle lettre voulez-vous proposer ? (Entrez 0 pour arrêter le jeu)\n").upper()
    #Vérifier que cette lettre n'est pas déja utilisée, ou qu'il s'agit bien d'une lettre.
    while(((char.upper() < "A" or char.upper() > "Z") or already_used(char) or len(char) != 1) and char != "0"):
        if(char.upper() < "A" or char.upper() >"Z" or len(char) !=1):
            print("Veuillez entrer une lettre valide !\n")
        else:
            print("Vous avez déja essayé cette lettre !\n")
        char = input("Quelle lettre voulez-vous proposer ? (Entrez 0 pour arrêter le jeu)\n").upper()
    if(char == "0"):
        print("Fermeture du jeu")
        exit()
    #Ajoute la lettre dans les lettres testées.
    charTested.append(char)
    return char