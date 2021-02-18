from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(start_text, shift_amount, cipher_direction):
  end_text=""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position >= len(alphabet):
        end_text += alphabet[new_position%len(alphabet)]
      else:
        end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"The {cipher_direction}d text is {end_text}")
  
ans="yes"

while ans != "no":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
  ans = input("Do you want to continue 'yes' or 'no' : ")
  if ans == "no":
    print('GoodBye')
