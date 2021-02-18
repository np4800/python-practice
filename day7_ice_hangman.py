import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

print(logo)
random_word = random.choice(word_list)
print(random_word)

count = 0
display=[]
str = ""
for _ in range(len(random_word)):
  display +="_"

end_of_game = False
lives = 6

while not end_of_game:
  guess_letter = input("Guess the letter: ")
  if guess_letter in display:

    print("You've already guessed this letter")

  for position in range(len(random_word)):
    letter = random_word[position]
   
    if letter == guess_letter.lower():
      display[position] = letter
  
  if guess_letter.lower() not in display:
    print(f"Guessed letter {guess_letter.lower()} is not there in the word. Try again!")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose")
 
  print(f"{' '.join(display)}")
  if "_" not in display:
    print("You Won")
    end_of_game = True
  print(stages[lives])
print(display)
