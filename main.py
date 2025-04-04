import random
#Variable globale:
charTested = []
charFound = []
restingLives = 6
data = []

#Tester si une lettre est déja utilisée:
def already_used(char):
    return (char in charTested)

#Tester si une lettre est présente dans le mot à deviner et ajouter dans la liste des lettres trouvées
def is_in_word(char, word):
    if char.upper() in word.upper():
        charFound.append(char.upper())
        return True
    else:
        return False

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

#Sépare le mot dans une liste
def split_word(word):
    charToFind = [char for char in word]
    return charToFind

#Vérifie si le mot est trouvé
def is_find(word):
    for char in word:
        if char.upper() not in charFound:
            return False
    return True

#Récupère la liste des mots dans donnees.txt
file = "data.txt"
with open(file) as dataFile:
    data = [line.strip() for line in dataFile.readlines()]

#Récupère un mot aléatoirement dans les données
def pick_random_word(data):
    i = random.randint(0,len(data)-1)
    return data.pop(i)

#Permet l'affichage du mot sous forme semi-caché
def print_word(word):
    for char in word:
        print(char if char in charFound else "_", end=" ")
    print("\n\n")
        
#Boucle principale du jeu
rep = ""
print("Bienvenue dans le jeu du Pendu ! Commençons :)\n")
while(rep == ""):
    ("Choix d'un nouveau mot . . .")
    if data == []:
        print("Oups, vous avez épuisée la base de données...")
        exit()
    wordToFind = pick_random_word(data)
    charFound = [wordToFind[0]]
    charTested.clear()
    charTested.append(wordToFind[0])
    restingLives = 6
    while(not is_find(wordToFind)):
        print_word(wordToFind)
        char = prop_letter()
        if(is_in_word(char, wordToFind)):
            print("\nBien vu ! Cette lettre est dans le mot à trouver")
        else:
            restingLives -=1
            print(f"\nDommage, cette lettre n'est pas dans le mot\nIl vous reste {restingLives} vies")
            if(restingLives == 0):
                print(f"Vous n'avez plus de vie ! Le mot était : {wordToFind}")
                rep = input("Tapez 'entrée' pour continuer à jouer, ou autre chose si vous voulez arrêter.")
                if rep == "":
                    break
                else:
                    print("Fermeture du jeu.")
                    exit()
    if(restingLives >0):
        print(f"\nFélicitation vous avez trouvé le mot : {wordToFind}\n")
        rep = input("Tapez 'entrée' pour continuer à jouer, ou autre chose si vous voulez arrêter.")
        if rep != "":
            print("Fermeture du jeu.")
            exit()
        
    