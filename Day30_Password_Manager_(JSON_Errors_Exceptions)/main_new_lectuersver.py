# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

"""
Catch the KeyError when a user enters a character that is not in the dictionary.
Provide feedback to the user when an illegal word was entered.
Continue prompting the user to enter another word until they enter a valid word.
"""


from pathlib import Path
import pandas

current_dir = Path(__file__).parent
data = pandas.read_csv(current_dir / "nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print("Created phonetic dictionary:", phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print("Output:", output_list)

generate_phonetic()