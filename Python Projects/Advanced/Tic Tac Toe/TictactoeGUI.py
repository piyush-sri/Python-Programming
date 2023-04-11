from tkinter import Tk, Label, Button,Frame
import random

#creating a window
screen = Tk()
#adding a title to window
screen.title(" "*40+"Tic Tac Toe Game")
#fixing the constant size of the screen
screen.geometry("400x500")

def newGame():
    global player
    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

def next_turn(row, column):
    global player

    if buttons[row][column]["text"] == "" and check_winner() is False:

        if player == players[0]:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))
            elif check_winner() == "Tie":
                label.config(text=("TIE"))
        else:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
            elif check_winner() == "Tie":
                label.config(text=("TIE"))


def check_winner():

    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] ==buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_space() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="red")

        return "Tie"
    else:
        return False


def empty_space():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True



players=["X", "O"]
player = random.choice(players)

label = Label(screen, text=player + " Turns ", font=('consolas',40))
label.pack()

resetButton = Button(screen, text="restart", font=('consolas', 20), command=newGame)
resetButton.pack(side="top")

frame = Frame(screen)
frame.pack()
buttons=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("consolas",40), width=4, height=1, command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)



#stopping the screen to wait until close button is clicked
screen.mainloop()
