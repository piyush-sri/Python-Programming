import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

word_list=["Python","Interpreter","Compiler","Bytecode","Github","Repository",
           "OpenSource","OneLinerNotes"]
chosen_word=random.choice(word_list)
print(logo)
lmt=len(chosen_word)
live=6
display=[]
for k in range(lmt):
    display+="_"
print(display)

end_Of_game=False

while  not end_Of_game:
    guess=input("Guess a Letter: ")
    #os.system('CLS')
    if guess in display:
        print(f"You've already guessed {guess}")
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        live-=1
        if live==0:
            end_Of_game=True
            print("You Lose!!")
    #character verification
    for i in range(lmt):
        letter=chosen_word[i]
        if letter==guess:
            display[i]=letter

    print(display)
        
    if "_" not in display:
        end_Of_game=True
        print("You Win.")
    print(stages[live])
