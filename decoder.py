from sys import exit

while True:
    # prompt for file name
    encode_file = input('Enter filename or exit: ')
    if encode_file.lower() == 'exit' or len(encode_file) == 0:
        exit()
    
    pass_len = input('Enter password length: ')
    # trying to convert input to a number - if not, asking again.
    while type(pass_len) != int: 
        try:
            pass_len = int(pass_len)
        except:
            print('Please enter a number.')
            pass_len = input('Number of words: ')
            
    if pass_len == 0:
        exit()

    password = []
    count = 1
    while count <= pass_len:
        try:
            code = int(input(f'Entry {count}: '))
            password.append(code)
            count += 1
        except ValueError:
            # exits because don't want to give a hint to what type of code it should be.
            print('Incorrect code.')
            exit()

    # open file
    words = []
    with open(f'{encode_file}.txt', 'r') as file:
        content = file.read().split()
        for word in content:
            words.append(word)

    # return passcode list
    for dex in password:
        print(words[dex])
