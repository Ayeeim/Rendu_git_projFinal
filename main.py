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