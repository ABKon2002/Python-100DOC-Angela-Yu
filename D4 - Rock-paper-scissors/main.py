asci = {
    'rock' : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'paper' : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
'scissors' : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
}

#Write your code below this line 👇

import random

user = input("Choose 'rock'(0), 'paper'(1) or 'scissors'(2): ")

if user == '0':
    user = 'rock'
elif user == '1':
    user = 'paper'
elif user == '2':
    user = 'scissors'

print("\nUser's choice:")
user_choice = user.lower()
print(asci[user_choice])

AI = ['rock', 'scissors', 'paper']
AI_choice = random.choice(AI)

print("\nAI's choice:")
print(asci[AI_choice])


# RPS rules
if user_choice == 'rock' and AI_choice == 'scissors':
    print("You win, fair! :)")
elif user_choice == 'rock' and AI_choice == 'paper':
    print("You lose :(")
elif user_choice == 'scissors' and AI_choice == 'paper':
    print("You win, fair! :)")
elif user_choice == 'scissors' and AI_choice == 'rock':
    print("You lose :(")
elif user_choice == 'paper' and AI_choice == 'rock':
    print("You win, fair! :)")
elif user_choice == 'paper' and AI_choice == 'scissors':
    print("You lose :(")
else:
    print("Its a draw :|")

print("Thanks for playing!")