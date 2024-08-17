from wonderwords import RandomWord
from random import randrange, choice
import string

print('Please wait, generating random sets... this will take a few minutes.')
random = RandomWord()
doc_size = 1000
# create list of random characters
random_words = [random.word() for _ in range(doc_size//3)]
random_letters = [''.join((choice(string.ascii_letters))
                          for _ in range(randrange(5, 15))) for _ in range(doc_size//3)]
random_characters = [''.join((choice(string.ascii_letters + string.punctuation))
                             for _ in range(randrange(5, 15))) for _ in range(doc_size//3)]

# merges random character lists into one list
text_list = []
for word in random_words:
    if word not in text_list:
        try:
            dex = randrange(len(text_list))
            text_list.insert(dex, word)
        except ValueError:
            text_list.append(word)
    for letter in random_letters:
        if letter not in text_list:
            dex = randrange(len(text_list))
            text_list.insert(dex, letter)
        for char in random_characters:
            if char not in text_list:
                dex = randrange(len(text_list))
                text_list.insert(dex, char)

# prompt for file name
print('\n')
encode_file = input('Enter file name: ')

# 12-word passcode
password = []
count = 1
while count <= 12:
    code = input(f'Word {count}: ')
    password.append(code)
    count += 1

# randomly insert words for password into random list
for pwd in password:
    index = randrange(len(text_list))
    text_list.insert(index, pwd)

# write list of random words to text file for saving
with open(f'{encode_file}.txt', 'w') as file:
    for word in text_list:
        file.write(f'{word} ')

code = [text_list.index(word) for word in password]  # creates a unique one-time passcode
# would like for this to be a max six length code - possible?
print('\n')
print(f'PLEASE WRITE DOWN:')
count = 1
for num in code:
    print(f'{count}: {num}')
    count += 1
