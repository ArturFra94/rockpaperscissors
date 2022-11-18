import tkinter as tk
from tkinter import *
import random

window = tk.Tk()
window.title("Rock paper scissors")
window.geometry('250x300')
window.resizable(True, True)
window.eval('tk::PlaceWindow . center')



def rock():
    global rockint, computerrandom,paperint,scissorint, winner
    playeroption.set("Rock")
    computeroption.set(".....")
    rockint = 1
    paperint = 0
    scissorint = 0
    computerrandom = random.randint(1,3)
def paper():
    global rockint, computerrandom,paperint,scissorint, winner
    playeroption.set("Paper")
    computeroption.set(".....")
    rockint = 0
    paperint = 2
    scissorint = 0
    computerrandom = random.randint(1, 3)
def scissors():
    global rockint, computerrandom,paperint,scissorint, winner
    playeroption.set("Scissors")
    computeroption.set(".....")
    rockint = 0
    paperint = 0
    scissorint = 3
    computerrandom = random.randint(1, 3)

def play():
    computeroption.set(computerrandom)
    if rockint == 1:
        if computeroption.get() == "1":
            winner.set("Tie")
            computeroption.set("Rock")
        elif computeroption.get() == "2":
            winner.set("Computer wins")
            computeroption.set("Paper")
        elif computeroption.get() == "3":
            winner.set("Player wins")
            computeroption.set("Scissors")
    if paperint == 2:
        if computeroption.get() == "1":
            winner.set("Player wins")
            computeroption.set("Rock")
        elif computeroption.get() == "2":
            winner.set("Tie")
            computeroption.set("Paper")
        elif computeroption.get() == "3":
            winner.set("Computer wins")
            computeroption.set("Scissors")
    if scissorint == 3:
        if computeroption.get() == "1":
            winner.set("Computer wins")
            computeroption.set("Rock")
        elif computeroption.get() == "2":
            winner.set("Player wins")
            computeroption.set("Paper")
        elif computeroption.get() == "3":
            winner.set("Tie")
            computeroption.set("Scissors")




frameempty0 = Label(window, text="")
frameempty0.grid(column=1, row=2, rowspan=2)

frameempty1 = Label(window, text="")
frameempty1.grid(column=2, row=2, columnspan=6)

framechoose = LabelFrame(window, text='Choose your move', bg='white')
framechoose.grid(column=2, row=3, columnspan=6)

rock_button = Button(
    framechoose,
    text='Rock',
    command=rock
)
rock_button.grid(column=2, row=3)

paper_button = Button(
    framechoose,
    text='Paper',
    command=paper
)
paper_button.grid(column=3, row=3)

scissors_button = Button(
    framechoose,
    text='Scissors',
    command=scissors
)
scissors_button.grid(column=4, row=3)

frameempty2 = Label(window, text="")
frameempty2.grid(column=2, row=4, columnspan=7)

playeroption = StringVar()
playeroption.set("Choose")

playerlabel = Label(window, text='Player option', bg='white', font=('Times New Roman', 12))
playerlabel.grid(column=2, row=8, columnspan=3)
optionlabel = Label(window, textvariable=playeroption, bg='white', font=('Times New Roman', 12), fg="red")
optionlabel.grid(column=5, row=8)

computeroption = StringVar()
computeroption.set("Choose")

computerlabel = Label(window, text='Computer option', bg='white', font=('Times New Roman', 12))
computerlabel.grid(column=2, row=9, columnspan=3)
optionlabel = Label(window, textvariable=computeroption, bg='white', font=('Times New Roman', 12), fg="red")
optionlabel.grid(column=5, row=9)

frameempty3 = Label(window, text="")
frameempty3.grid(column=2, row=10, columnspan=7)

play_button = Button(
    window,
    text='Play',
    command=play
)
play_button.grid(column=4, row=11, columnspan=2)

winner = StringVar()
winner.set("....")

computerlabel = Label(window, text='Winner is: ', bg='white', font=('Times New Roman', 12))
computerlabel.grid(column=2, row=12, columnspan=3)
optionlabel = Label(window, textvariable=winner, bg='white', font=('Times New Roman', 12), fg="red")
optionlabel.grid(column=5, row=12)

window.mainloop()