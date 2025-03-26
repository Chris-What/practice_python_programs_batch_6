#Batch 6 - Program 1
#Remove beginning spaces from a string without using lstrip()

#ask the user to input a string with spaces in the beginning and initialize a counter for the spaces
string = input("Enter a string with spaces in the beginning: ")
spaces = 0

#loop through the string to count the beginning spaces by finding the index where the first non-space character appears
while spaces < len(string) and string[spaces] == " ":
    spaces += 1

#create new string where it starts at the first index with a non-space character, essentially removing every space in the beginning
new_string = string[spaces:]

print(new_string)