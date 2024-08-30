from wonderwords import RandomWord
from random import randrange, choice
import string


# prompt for file name
encode_file = input('Filename: ')

pass_len = input('Number of words: ')
# trying to convert input to a number - if not, asking again.
while type(pass_len) != int: 
    try:
        pass_len = int(pass_len)
    except:
        print('Please enter a number.')
        pass_len = input('Number of words: ')

document_len = input('Amount of randomly generated words: ')
# trying to convert input to a number - if not, asking again.
while type(document_len) != int:
    try:
        document_len = int(document_len)
    except:
        print('Please enter a number.')
        document_len = input('Amount of randomly generated words: ')

if document_len >= 500:
    print('Please wait, generating random words... this will take a few minutes.')

random = RandomWord()
# create list of random characters
random_words = [random.word() for _ in range(document_len//3)]
random_letters = [''.join((choice(string.ascii_letters))
                          for _ in range(randrange(5, 15))) for _ in range(document_len//3)]
random_characters = [''.join((choice(string.ascii_letters + string.punctuation))
                             for _ in range(randrange(5, 15))) for _ in range(document_len//3)]

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

password = []
count = 1
while count <= pass_len:
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

print('\n')
print(f'PLEASE WRITE DOWN - these will be used to recover your password:')
count = 1
for num in code:
    print(f'{count}: {num}')
    count += 1
