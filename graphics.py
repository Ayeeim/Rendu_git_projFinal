from tkinter import *

lstButton = []

#Pas encore implémenté
def play_menu():
    return 0
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

#Fonction factice à récupérer dans le main
def hidden_word(word):
    return "T _ _ T"
