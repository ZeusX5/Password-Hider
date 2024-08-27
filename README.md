This is my first project and the idea is a password 'hider'. Running the encoder script will generate three random lists of different types of words/characters and then merge into one list.
It then prompts the user for a file name, writes as a .txt file by default, and then prompts for 12-word password (geared towards crypto wallets, but will most likely update to user's choice). Then it randomly inserts the given password into the list of random words and characters.
After doing so, the list will be written to a file and then generate a code for  retrieving the password. This is a one-time unique code - must copy down because it won't be the same if ran again. 

Running the decoder script will open the given file name, defaulted to .txt file, and create a list from the parsed strings. 
Prompts user for the number code, generated from the encoder script, and uses it to retrieve password in order as entered. 
