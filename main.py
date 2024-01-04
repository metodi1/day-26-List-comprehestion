# number = [1,2,3]
# new_numbres = [n+1 for n in number]
# print(new_numbres)

# name = "Metodi"
# letter_list = [letter for letter in name]
# print(letter_list)

# new_list = [a*2 for a in range(1,5)]
# print(new_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# new_names = [name.upper() for name in names if len(name)>5]
# print(new_names)

import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# student_score = {name:random.randint(1,100) for name in names}
# print(student_score)
#
# student_score = {'Alex': 82, 'Beth': 42, 'Caroline': 64, 'Dave': 8, 'Eleanor': 39, 'Freddie': 82}
# pass_student = {name:score for (name,score) in student_score.items() if score >= 60}
# print(pass_student)

import pandas

data_nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# #TODO 1. Create a dictionary
nato_dict = {row.letter: row.code for (index, row) in data_nato.iterrows()}

word = input("Enter a word: ").upper()
words = [nato_dict[letter] for letter in word]
print(words)

