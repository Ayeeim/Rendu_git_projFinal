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

#Permet l'affichage du mot sous forme semi-caché
def print_word(word):
    for char in word:
        print(char if char in charFound else "_", end=" ")
    print("\n\n")
