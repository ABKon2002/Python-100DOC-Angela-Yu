hangman_rules = [
    "1. The computer thinks of a word.",
    "2. You try to guess the word letter by letter.",
    "3. However, you have a limited number of incorrect guesses.",
    "4. Correct guesses reveal letter positions in the word.",
    "5. Incorrect guesses adds a part to the hangman drawing.",
    "6. You win by guessing the word before the drawing is complete.",
    "7. You lose, if the drawing is completed before the word is guessed.",
    "Good luck! Have fun playing :)"
]

def display_rules():
    print("\n********* RULES *********\n")
    for rule in hangman_rules:
        print(rule)
        print()