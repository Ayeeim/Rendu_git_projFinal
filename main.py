#Variable globale:
charTested = []
charFound = []
restingLives = 6

#Tester si une lettre est présente dans le mot à deviner et ajouter dans la liste des lettres trouvées
def is_in_word(char, word):
    if char.upper() in word.upper():
        charFound.append(char.upper())
        return True
    else:
        return False
    
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