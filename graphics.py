from tkinter import *

lstButton = []

#Fonction factice à récupérer dans le main
def hidden_word(word):
    return "T _ _ T"

#Pas encore implémenté
def play_menu():
    playMenu = Tk()

    playMenu.config(bg="#ffcd00")
    playMenu.geometry("1080x720")

    frame = Frame(playMenu, bg="#ffcd00")
    frame.pack(expand=YES)

    title = Label(frame, text=hidden_word("TEST"), font=("Courrier",40, "bold"), fg="white", bg="#ffcd00", pady=10)
    title.pack()

    canva = Canvas(frame, width=300, height=300, bg="#ffcd00", highlightthickness=0)
    canva.pack()

    letters = Frame(frame, bg="#ffcd00")
    letters.pack(expand=YES)

    #Création des boutons:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    global lstButton
    row= 0
    column = 0
    for char in alphabet:
        button = Button(letters, text=char, width=5, height=2, padx=2, pady=2)
        button.grid(row=row, column= column)
        lstButton.append(button)
        column += 1
        if column ==10:
            row +=1
            if(row == 2):
                column = 2
            else:
                column =0
    playMenu.mainloop()

def start_menu():
    global window
    window.config(bg="#ffcd00")
    window.geometry("1080x720")
    frame = Frame(window, bg="#ffcd00")
    frame.pack(expand=YES)
    title = Label(frame, text="Jeu du Pendu", font=("Courrier",40, "bold"), fg="white", bg="#ffcd00", pady=75)
    title.pack()

    button = Button(frame, bg="#ffcd00", fg="white", font=("Courrier",20, "bold"), text="Jouer", relief=SUNKEN, command=play_menu)
    button.pack(fill=X)
    window.mainloop()

window = Tk()
start_menu()



