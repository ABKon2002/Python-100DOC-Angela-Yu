# Modules
import random
import word_data
from asciiArt import stages, logo
import rules
from time import sleep
from replit import clear

# Intro banner
print(logo)
print("\nWelcome to Hangman! I am Lil_Shit_Niga, your host for today's game.")
rulesChoice = input("Would you like to know the rules of the game? (y/n): ")
if rulesChoice == 'y':
    rules.display_rules()
    sleep(7)

topicChoice = int(
    input('''
What topic would you like to play?
1. Fruits and Vegetables
2. Food items
3. Sports
4. Iconic Personalities
5. Any
Enter your choice: '''))

# Preparing word pool based on chosen topic
if topicChoice == 1:
    words = word_data.fruggies
elif topicChoice == 2:
    words = word_data.food_words
elif topicChoice == 3:
    words = word_data.sports_words
elif topicChoice == 4:
    words = word_data.iconic_personalities
elif topicChoice == 5:
    words = word_data.genAny()
else:
    print("Invalid choice. Please try again.")
    exit()

currentWord = random.choice(words)
wordList = [char for char in currentWord]
displayList = ['_'] * len(currentWord)
displayWord = ' '.join(displayList)
# print(f"Word => {currentWord}")  ** only for debugging
guesses = []
lives = 6

# Gameplay
print(f"\nWord: {displayWord}\n")
while '_' in displayList and lives > 0:
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print(f"You already guessed {guess}, Try again!")
        continue
    elif not guess.isalpha():
        print("Please enter a valid letter! Try again!")
        continue
    guesses.append(guess)

    clear()

    if guess in wordList:
        for i in range(len(wordList)):
            if wordList[i] == guess:
                displayList[i] = guess
        displayWord = ' '.join(displayList)
    else:
        lives -= 1
    print(f"\nStatus: {displayWord}")
    print(stages[lives])
    print("\n--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--\n")

if '_' not in displayList:
    print("You Win! Thank you for saving the man!")
else:
    print("You Lose. This man died :( Try Again saving another man!")
    print(f"The word was {' '.join(wordList)}")
