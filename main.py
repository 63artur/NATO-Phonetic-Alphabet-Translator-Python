import pandas
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
dictionary = {row.letter: row.code for _, row in nato.iterrows()}
print(dictionary)
answer = input("Enter a word: ").upper()
nato_translation = [print(f"{letter} for {dictionary[letter]}") for letter in answer if letter in dictionary]
