import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter:row.code for (index,row) in df.iterrows()}

#Method one
def generate_nato_code():
    word = input("Please enter a word to generate the Nato code for each letter: ").upper()
    try:
        nato_code = [nato_dictionary[letter] for letter in word]
    except KeyError:
        print("Please enter only letters in the alphabets")
        generate_nato_code()
    else:
        print(nato_code)

#call my function
generate_nato_code()

# #Method two
# try:
#     word = input("Please enter a word to generate the Nato code for each letter: ").upper()
#     for letter in word:
#         for (key, value) in nato_dictionary.items():
#             if letter != key:
#                 raise ValueError
# except ValueError:
#     should_continue = True
#     while should_continue:
#         print("Please enter only letters in the alphabets")
#         word = input("Please enter a word to generate the Nato code for each letter: ").upper()
#         for letter in word:
#             for (key, value) in nato_dictionary.items():
#                 if letter == key:
#                     should_continue = False
#                 else:
#                     continue
#
# #alternative
# # nato_code = [nato_dictionary[letter] for letter in word]
# finally:
#     nato_code = [value for letter in word for (key,value) in nato_dictionary.items() if letter == key]
#
#     print(nato_code)
#
