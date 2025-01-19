import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Create a dictionary of the phonetic alphabet.
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

#Take a word as input and print the phonetic letters in the word.
def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("You must only enter letters in the alphabet.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()