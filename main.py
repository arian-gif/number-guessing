import art
import random

def display_logo():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")

def get_difficulty():
    difficulty=""
    while difficulty != "easy" and difficulty != "hard":
        difficulty = input("I'm thinking of a number between 1 and 100. Choose a difficulty. Type 'easy' or 'hard': \n").lower()
        if difficulty != "easy" and difficulty != "hard":
            print("incorrect input please try again\n")
    return difficulty

def set_attempts(difficulty):
    return 10 if difficulty == "easy" else 5

def play_game(attempts, number):
    has_won = False
    while not has_won and attempts > 0:
        print(f"You have {attempts} remaining to guess the number:\n")
        guess = int(input("Make a guess:\n"))
        if guess > number:
            print("Too high\n")
        elif guess < number:
            print("Too low\n")
        elif guess == number:
            has_won = True
        attempts -= 1
    return has_won

def display_result(has_won, number):
    if has_won:
        print(f"You got it! The answer was {number}")
    else:
        print(f"Better luck next time, the answer was {number}")

def main():
    display_logo()
    difficulty = get_difficulty()
    attempts = set_attempts(difficulty)
    number = random.randint(1, 100)
    has_won = play_game(attempts, number)
    display_result(has_won, number)

main()





