This is my first project and the idea is a password 'hider'. Running the encoder script will take in a few prompts from the user and then generate three random lists of different types of words/characters and then merge into one list.
Then it randomly inserts the given password into the list of random words and characters. After doing so, the list will be written to a file and then generate a code for  retrieving the password. This is a one-time unique code - must copy down because it won't be the same if ran again. 

Running the decoder script will open the given file name, defaulted to .txt file, and create a list from the parsed strings. 
Prompts user for the number code, generated from the encoder script, and uses it to retrieve password in order as entered. 
