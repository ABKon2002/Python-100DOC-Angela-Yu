import pandas as pd

nato_df = pd.read_csv("D26 - List comprehensions\\nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (_, row) in nato_df.iterrows()}

def generate_phonetic():
    user_ip = input("Enter a word: ").upper()
    output_list = []
    try:
        output_list = [nato_dict[letter] for letter in user_ip]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()
