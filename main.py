#Variable globale:
charTested = []
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
    charTested.append(har)
    return char