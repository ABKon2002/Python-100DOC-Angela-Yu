#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
print(logo)
print()
print("I have guessed a number between 1 and 100. Can you guess it?")

from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def play(guess, actual, turns):
    if turns <= 0:
        print("You have ran out of turns. You lose.")
        return 
    if guess > actual:
        print("Too high :(")
        print("\n***********************************************\n")
        print("You have {} attempts remaining!".format(turns - 1))
    elif guess < actual:
        print("Too low :)")
        print("\n***********************************************\n")
        print("You have {} attempts remaining!".format(turns - 1))
    else:
        print(f"You got it! The answer was {actual}")
        print("Thanks for playing!")
        return
    newGuess = int(input("Guess again: "))
    play(newGuess, actual, turns - 1)

print("Based on the difficulty you choose, you will have a certain number of attempts to guess the number.\n")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = EASY_LEVEL_TURNS
elif difficulty == 'hard':
    attempts = HARD_LEVEL_TURNS
else:
    print("Invalid input. Please try again.")
    exit(1)

print("You have {} attemps to guess the number.\n".format(attempts))

my_guess = randint(1, 100)

valid_guess = False

while not valid_guess:
    their_guess = int(input("Make a guess: "))
    if their_guess < 1 or their_guess > 100:
        print("Invalid guess. Please guess a number between 1 and 100.")
    else:
        valid_guess = True

play(their_guess, my_guess, attempts)
