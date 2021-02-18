import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = ["rock","paper","scissors"]
player1 = int(input('Enter what you like "0 for rock" "1 for paper" "2 for scissors" '))
player2 = random.randint(0,2)
print(f"Player1 = {player1} and Player2 = {player2}")

if player1 >= 3:
  print(f"Invalid Choice")


if player1 == player2:
  print("Game is Draw")
  if game[player1] == "rock":
    print(f"Player1 said \n {rock}")
    print(f"Player2 said \n {rock}")
  if game[player1] == "paper":
    print(f"Player1 said \n {paper}")
    print(f"Player2 said \n {paper}")
  if game[player1] == "scissors":
    print(f"Player1 said \n {scissors}")
    print(f"Player2 said \n {scissors}")



# rule-1: rock wins against sissors
if game[player1] == "rock" and game[player2] == "scissors":
  print("Player-1 wins")
  print(f"Player 1 said \n {rock}")
  print(f"Player 2 said \n {scissors}")
elif game[player1] == "scissors" and game[player2] == "rock":
  print(f"Player 1 said \n {scissors}")
  print("Player 2 wins")
  print(f"Player 2 said \n {rock}")

# rule-2: Scissors wins against paper
if game[player1] == "scissors" and game[player2] == "paper":
  print("Player 1 wins")
  print(f"Player 1 said \n {scissors}")
  print(f"Player 2 said \n {paper}")
elif game[player1] == "paper" and game[player2] == "scissors":
  print(f"Player 1 said \n {paper}")
  print("Player 2 wins")
  print(f"Player 2 said \n {scissors}")

# rule-3: Paper wins against rock
if game[player1] == "paper" and game[player2] == "rock":
  print("Player 1 wins")
  print(f"Player 1 said \n {paper}")
  print(f"Player 2 said \n {rock}")
elif game[player1] == "rock" and game[player2] == "paper":
  print(f"Player 1 \n {rock}")
  print("Player 2 wins")
  print(f"Player 2 \n {paper}")
