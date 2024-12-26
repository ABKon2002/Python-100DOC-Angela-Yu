import pandas as pd

nato_df = pd.read_csv("D26 - List comprehensions\\nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (_, row) in nato_df.iterrows()}

user_ip = input("Enter a word: ").upper()
output_list = [nato_dict[letter] for letter in user_ip]
print(output_list)
