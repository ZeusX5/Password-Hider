# prompt for file name
encode_file = input('Enter file: ')

# prompt for 12 index password
password = []
count = 1
while count <= 12:
    code = int(input(f'Word {count}: '))
    password.append(code)
    count += 1

# open file
words = []
with open(f'{encode_file}.txt', 'r') as file:
    content = file.read().split()
    for word in content:
        words.append(word)

# return passcode list
for dex in password:
    print(words[dex])
