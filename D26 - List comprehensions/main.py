import pandas as pd

#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_df = pd.read_csv("D26 - List comprehensions\\nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_ip = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in user_ip]
print(output_list)
