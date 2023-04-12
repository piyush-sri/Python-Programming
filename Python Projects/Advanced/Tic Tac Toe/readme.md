# Line By Line Explanation of Source Code

1. **Importing necessary modules**:
```python
from tkinter import Tk, Label, Button, Frame
import random
```
Here, we are importing `Tk`, `Label`, `Button`, and `Frame` from the `tkinter module`. We are also importing the `random module` to randomly select the player who goes first.

2. **Creating a window**:
```python
screen = Tk()
screen.title(" "*40+"Tic Tac Toe Game")
screen.geometry("400x500")
```
Here, we are creating a window using the `Tk()` constructor of the `Tkinter module`. We set the title of the window to `Tic Tac Toe Game` and fixed the size of the screen to be 400x500.

3. **Creating a new game**:
```python
def newGame():
    global player
    player = random.choice(players)
    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")
```
This function is used to start a new game. It selects a random player to go first using the `random.choice()` method, updates the label to display whose turn it is, and resets the buttons to be blank.

4. **Changing turns**:
```python
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
```
This function is used to change turns between the players. It checks if the button clicked is blank and if there is no winner yet. If the conditions are met, it updates the button with the player's symbol, checks for a winner, and updates the label accordingly. If there is a winner or a tie, the label is updated accordingly.

5. **Checking for a winner**:
 ```python
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
 ```
 This function checks if any player has won the game or if there is a tie. The function returns True if any player wins the game, `Tie` if there is a tie, or False if the game is still in progress.

The function first checks if any player has won the game horizontally, by comparing the text on buttons in each row. If the texts on all buttons in a row are the same and not empty, the buttons in that row are highlighted with a green background color, and the function returns True.

The function then checks if any player has won the game vertically, by comparing the text on buttons in each column. If the texts on all buttons in a column are the same and not empty, the buttons in that column are highlighted with a green background color, and the function returns True.

The function then checks if any player has won the game diagonally, by comparing the text on buttons in both diagonals. If the texts on all buttons in a diagonal are the same and not empty, the buttons in that diagonal are highlighted with a green background color, and the function returns True.

If there is no winner and all the spaces are filled, the function highlights all the buttons with a red background color, indicating that the game has ended in a tie, and the function returns `Tie`.

If the game is still in progress, the function returns False.

6. **Checking for empty spaces**:
 ```python
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
 ```
 This function checks if there are any empty spaces left on the board. If all the spaces are filled, the function returns False. Otherwise, it returns True.
 
 7. `players list` and `player variable`:
 
 ```python
 players=["X", "O"]
 player = random.choice(players)
```

 `players` is a list containing the two possible values that can be assigned to the player variable: `"X"` and `"O"`. The player variable is initially assigned a random value from the players list.
 
