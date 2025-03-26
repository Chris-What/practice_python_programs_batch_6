#Batch 6 - Program 1

#ask the user to input a string with spaces in the beginning and initialize a counter for the spaces
string = input("Enter a string with spaces in the beginning: ")
spaces = 0

#loop through the string to count the beginning spaces by finding the index where the first non-space character appears
while spaces < string and string[spaces] == " ":
    spaces += 1

#display new string