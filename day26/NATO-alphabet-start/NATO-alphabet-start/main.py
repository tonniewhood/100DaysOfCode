
import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")
# print(nato_data_frame)

nato_alphabet = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}

# print(nato_alphabet)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = list(input("Enter a name: "))

nato_name = [nato_alphabet[letter.upper()] for letter in name]

print(nato_name)
