logo=""" ___                        _                    
(  _`\                     ( )_  _               
| ( (_) _ __  _   _  _ _   | ,_)(_)   ___        
| |  _ ( '__)( ) ( )( '_`\ | |  | | /'___)       
| (_( )| |   | (_) || (_) )| |_ | |( (___        
(____/'(_)   `\__, || ,__/'`\__)(_)`\____)       
             ( )_| || |                          
             `\___/'(_)                          
 ___    _               ___   ___  _             
(  _`\ ( )            /'___)/'___)(_ )           
| (_(_)| |__   _   _ | (__ | (__   | |    __     
`\__ \ |  _ `\( ) ( )| ,__)| ,__)  | |  /'__`\   
( )_) || | | || (_) || |   | |     | | (  ___/   
`\____)(_) (_)`\___/'(_)   (_)    (___)`\____)   
                                                 
                                                 
 ___                                             
(  _`\                                           
| ( (_)   _ _   ___ ___     __                   
| |___  /'_` )/' _ ` _ `\ /'__`\                 
| (_, )( (_| || ( ) ( ) |(  ___/                 
(____/'`\__,_)(_) (_) (_)`\____)                 
                                                 
                                                 """   
 
                                                                                                                                                                                       
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #fixing the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")
 
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")

    
