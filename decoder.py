# prompt for file name
encode_file = input('Enter file: ')

# prompt for 12 indexes
passcode_1 = int(input('Passcode 1: '))
passcode_2 = int(input('Passcode 2: '))
passcode_3 = int(input('Passcode 3: '))
passcode_4 = int(input('Passcode 4: '))
passcode_5 = int(input('Passcode 5: '))
passcode_6 = int(input('Passcode 6: '))
passcode_7 = int(input('Passcode 7: '))
passcode_8 = int(input('Passcode 8: '))
passcode_9 = int(input('Passcode 9: '))
passcode_10 = int(input('Passcode 10: '))
passcode_11 = int(input('Passcode 11: '))
passcode_12 = int(input('Passcode 12: '))

# retrieve 12-word using index list
code = [passcode_1, passcode_2, passcode_3, passcode_4, passcode_5, passcode_6,
        passcode_7, passcode_8, passcode_9, passcode_10, passcode_11, passcode_12]

# open file
words = []
with open(f'{encode_file}.txt', 'r') as file:
    content = file.read().split()
    for word in content:
        words.append(word)

# return passcode list
for dex in code:
    print(words[dex])
