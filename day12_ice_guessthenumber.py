import random

EASY_TURNS = 5
HARD_TURNS = 10
flash_number = random.randint(1,100)

def check_answer(guess,answer,turns):
    if guess < answer:
        print("Too low!")
        return turns - 1
    elif guess > answer:
        print("Too high!")
        return turns - 1
    else:
        print("You guessed it right! Indeed!")

def set_difficulty():
    game_level = input("Choose a difficulty level, type 'easy' or 'hard': ")    
    if game_level == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def play_game():
    print("Welcome to Guessing Game!")
    print("I am thinking a number between 1 and 100")
    print(f"Psst, the correct answer is: {flash_number}")
    answer = flash_number
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)

        if turns == 0:
            print("You ran out of attempts! ")
            return
        elif guess != answer:
            print("Guess again")
    
play_game()

