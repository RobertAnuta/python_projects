from data import alphabet
from art import logo

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def cipher(text,shift,direction):    
  output_text = ""
  
  if direction == "decode":
    shift  *= -1
  #loop thru the input text
  for character in text:
    if character in alphabet:
      position = alphabet.index(character)
      encrypted_position = (position + shift) % (len(alphabet))
      output_text += alphabet[encrypted_position]
    #if the character is a symbol, don't change it and add it to the output text
    else:
      output_text += character
  print(f"\nThe {direction}d text is {output_text}")
  
  #play again functionality
  play_again = input("Do you want to encript or decript more? Y or N\n").lower()
  
  if play_again == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    cipher(text,shift,direction)
  else:
    print("\nGoodbye")

if __name__ == "__main__":
    cipher(text,shift,direction)
