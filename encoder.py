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
password = []
count = 1
while count <= 12:
    code = input(f'Word {count}: ')
    password.append(code)
    count += 1

# randomly insert words for password into random list - can be list comp?
for pwd in password:
    index = randrange(len(text_list))
    text_list.insert(index, pwd)

# write list of random words to text file for saving
with open(f'{encode_file}.txt', 'w') as file:
    for word in text_list:
        file.write(f'{word} ')

code = [text_list.index(word) for word in password]  # creates a unique one-time passcode
print(code)
