from wonderwords import RandomWord
from random import randrange, choice
import string


random = RandomWord()
doc_size = 50
# create list of random characters
random_words = [random.word() for _ in range(doc_size//3)]
random_letters = [''.join((choice(string.ascii_letters))
                          for _ in range(randrange(5, 15))) for _ in range(doc_size//3)]
random_characters = [''.join((choice(string.ascii_letters + string.punctuation))
                             for _ in range(randrange(5, 15))) for _ in range(doc_size//3)]

# merges random character lists into one list
text_list = []
for word in random_words:
    text_list.append(word)
    for letter in random_letters:
        text_list.append(letter)
        for char in random_characters:
            text_list.append(char)

# prompt for file name
encode_file = input('Enter file name: ')

# 12-word passcode
input_1 = input('Word 1: ')
input_2 = input('Word 2: ')
input_3 = input('Word 3: ')
input_4 = input('Word 4: ')
input_5 = input('Word 5: ')
input_6 = input('Word 6: ')
input_7 = input('Word 7: ')
input_8 = input('Word 8: ')
input_9 = input('Word 9: ')
input_10 = input('Word 10: ')
input_11 = input('Word 11: ')
input_12 = input('Word 12: ')

password = [input_1, input_2, input_3, input_4, input_5, input_6,
            input_7, input_8, input_9, input_10, input_11, input_12]

# randomly insert words for password into random list
for pwd in password:
    index = randrange(len(text_list))
    text_list.insert(index, pwd)

# write list of random words to text file for saving
with open(f'{encode_file}.txt', 'w') as file:
    for word in text_list:
        file.write(f'{word} ')

code = [text_list.index(word) for word in password]  # creates a unique one-time passcode
print(code)
