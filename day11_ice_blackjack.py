import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
## Calculate the score for the user and computer
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

## Create a deal_card() function that returns a random card for user and computer         
def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

## Compare the scores
def compare(user_score,computer_score):
  if user_score == computer_score:
    return "It was Pushed!"
  elif computer_score == 0:
    return "You lost! Computer got a Blackjack!"
  elif user_score == 0:
    return "You win! You got a Blackjack!"
  elif user_score > 21:
    return "Bust! You lost!"
  elif computer_score > 21:
    return "You win! Computer Bust"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lost!"


def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  should_continue = True

  while should_continue:
    print(logo)

    ## Deal the user and computer 2 cards each using deal_card() and append()
    for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())


    while not is_game_over:
      
      user_score = calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)

      print(f"  Your cards: {user_cards}, current score: {user_score}")
      print(f"  Computer's first card: {computer_cards[0]}")

      if user_score == 0 or computer_score == 0 or user_score > 21: 
        is_game_over = True
      else:
        user_should_deal = input("Type 'y' to draw a card 'n' to pass: ")
        if user_should_deal == "y":
          user_cards.append(deal_card())
        else:
          is_game_over = True ## game over for user

    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))
  
while input("Do you want to play, type 'y' or 'n' not to play: ") == "y":
  play_game()

