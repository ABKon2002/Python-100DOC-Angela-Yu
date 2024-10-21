from random import randint
from time import sleep
from replit import clear
from game_data import data, data1
from art import logo, vs

def get_random_account():
    """Get data from random account"""
    Data = data + data1
    return Data[randint(0, len(data) - 1)]

def format_data(account):
    """Formats an account data to a printable format"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

def check_answer(guess, follower1, follower2):
    """Checks the correctness of the answer"""
    if guess == 'higher':
        return follower1 >= follower2
    elif guess == 'lower':
        return follower1 <= follower2

def currHighScores(path = "user_data.txt"):
    high_scores = []
    with open(path, 'r') as f:
        data = f.readlines()
        records = [line.strip().split(',') for line in data]
        for record in records:
            recDict = {}
            recDict['User_Name'] = record[0].strip()
            recDict['User_High_Score'] = int(record[1])
            high_scores.append(recDict)
    return high_scores

def register(currHs):
    """Registers the user to keep track of their high scores in an involatile file."""
    print(logo)
    print()
    played_before = input("Have you played this before? (y/n): ")
    
    if played_before == 'y':
        name = input("What name did you play by? ")
        currHs_names = [hs['User_Name'] for hs in currHs]
        while name not in currHs_names:
            print(f"Sorry, {name} has not played before here.")
            print("Try from, ")
            for name in currHs_names:
                print(name)
            new_name = input("Would you like to register as a new user or try again with one of the names above? (new/try): ")
            if new_name == 'new':
                name = input("What name would you like to register as? ")
                print(f"Hello {name}, Enjoy the game!")
                return name
            elif new_name == 'try':
                name = input("What name did you play by? ")
        else:
            print(f"Hello {name}, Enjoy the game!")
            return name
    else:
        name = input("What name would you like to register as? ")
        print(f"Hello {name}, Enjoy the game!")
        return name

def writetofile(hscores, name, hscore, path = 'user_data.txt'):
    """Writes the user's name and high score to a file."""
    with open(path, 'w') as f:
        f.write(f"{hscores[0]['User_Name']},{hscores[0]['User_High_Score']}\n")
    
    with open(path, 'a') as f:
        for hs in hscores[1:]:
            f.write(f"{hs['User_Name']},{hs['User_High_Score']}\n")

def top_players(hscores):
    """Returns top 3 players with highest scores."""
    '''
    for hs in hscores:
        if len(top_players) < 3:
            top_players.append(hs)
        else:
            if hs['User_High_Score'] > top_players[2]['User_High_Score']:
                top_players[2] = hs
    '''
    top_players = sorted(hscores, key=lambda x: x['User_High_Score'], reverse=True)
    return top_players[:3]

def printLeaderboard(top_players):
    """Prints the leaderboard of top 3 players with highest scores."""
    print()
    print("\n********* Leaderboard *********\n")
    for i, player in enumerate(top_players):
        print(f"{i+1}. {player['User_Name']} - {player['User_High_Score']}")

def game(high_score = 0):
    print(logo)
    print()
    print("Welcome to the Higher or Lower Game!")
    print("However, this time, you will be comparing the number of Instagram followers of two given instagram accounts.")
    print("*** Warning: The data is not updated regularly, so the numbers may not be accurate. ***")
    print("\n*************************************************\n")

    curr_score = 0
    game_over = False
    A_acct = get_random_account()
    
    while not game_over:
        B_acct = get_random_account()
        while A_acct == B_acct:
            B_acct = get_random_account()
        
        print(f"Current score: {curr_score} \t\t\t\t High Score: {high_score}")
        print()
    
        print(f"Compare A: {format_data(A_acct)}")
        print(vs)
        print(f"Against B: {format_data(B_acct)}")
        
        print("\nWho has more followers?")
        guess = input("Type ('higher' / '>') or ('lower' / '<'): ")
        follower1 = A_acct['follower_count']
        follower2 = B_acct['follower_count']
        if guess == '>':
            guess = 'higher'
        elif guess == '<':
            guess = 'lower'
        guess = guess.lower()
        while guess not in ['higher', 'lower']:
            print("Invalid input. Please enter 'higher' or 'lower'.")
            guess = input("Type ('higher' / '>') or ('lower' / '<'): ")
            if guess == '>':
                guess = 'higher'
            elif guess == '<':
                guess = 'lower'
            guess = guess.lower()

        if check_answer(guess, follower1, follower2):
            curr_score += 1
            clear()
            print(logo)
            print(f"Current score: {curr_score} \t\t\t High Score: {high_score}")
            print()
            print("You're right!")
            print(f"{A_acct['name']} : {follower1} million followers")
            print(f"{B_acct['name']} : {follower2} million followers")
            print()
            A_acct = B_acct
            game_over = False
        else:
            print("Game Over! :(")
            print(f"{A_acct['name']} : {follower1} million followers")
            print(f"{B_acct['name']} : {follower2} million followers")
            print()
            game_over = True
            return curr_score


play_game = True
hs = 0
hscores = currHighScores()
name = register(hscores)
for i in range(3, 0, -1):
    print(f"Play in {i} seconds...")
    sleep(1)
clear()

while play_game:
    score = game(hs)
    if score > hs:
        hs = score
    play_game = input("Do you want to play again? (y/n): ")
    play_game = play_game.lower() == 'y'
    clear()

names = [data['User_Name'] for data in hscores]
if name in names:
    for record in hscores:
        if record['User_Name'] == name:
            if record['User_High_Score'] < hs:
                record['User_High_Score'] = hs
                print(f"Thank you for playing!, Your high score of {hs} has been recorded under the name of {name}. Come back to improve it :)")
            else:
                print(f"Thank you for playing!, You already have a better score of {record['User_High_Score']}.")
            break
else:
    hscores.append({'User_Name': name, 'User_High_Score': hs})
    print(f"Thank you for playing!, Your high score of {hs} has been recorded under the name of {name}. Come back to improve it :)")

print(logo)
print()
writetofile(hscores, name, hs)

printLeaderboard(top_players(hscores))
