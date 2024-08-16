The idea here is a passcode 'hider'. First running the encoder script to generate three random lists of different types of words/characters and then merge into one list.
It then prompts user for a file name, writes as a .txt file, and then prompts for 12-word password (geared towards crypto wallets). Then it randomly inserts password into list of random words and characters.
After doing so, the list will be written to file and then generate a code list of indexes of 12-word password in the order entered. This is a one-time unique code list - must copy down because it won't be the same if ran again. 

Running the decoder script will open the given file name, defaulted to .txt file, and create a list from the parsed strings. 
Prompts user for the 12 number code list, mentioned in line 3, and uses it to retrieve password in order as entered. 
