import random
from game_data import data
from art import logo2, vs

print(logo2)

# Generate a random number to chose for the the game data
def get_item():
    return random.choice(data)

# Create a funtion to compare and calculate the score
def declare_winner(a_fcount,b_fcount):
    if a_fcount > b_fcount:
        return "A"
    else:
        return "B"

# Save the comparsion item from the previous win and compare it with new item in the game list


# Function to play game
def game():
    end_game = False
    score = 0
    while not end_game:
        a = get_item()
        b = get_item()
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}")
        answer = input("Who has more followers. Type 'A' or 'B': ")
        winner = declare_winner(a['follower_count'],b['follower_count'])
        if winner.lower() == answer.lower():
            score += 1
            print(f"You win, score is: {score}")
        else:
            print(f"You win, score is: {score}")
            print("You lost!")
            end_game = True
# main function to ask the user input
game()