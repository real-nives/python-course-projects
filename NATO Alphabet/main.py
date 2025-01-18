import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary of the phonetic alphabet.
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#Take a word as input and print the phonetic letters in the word.
word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)