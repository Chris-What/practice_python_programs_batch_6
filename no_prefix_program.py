#Batch 6 - Program 2
#Remove a specified prefix in the beginning of a string without using removeprefix()

#ask the user to input a string and the prefix they want to be removed
string = input("Enter a string: ")
prefix = input("Enter prefix you want to remove: ")

#check if the string starts with the prefix and remove it from the string by making a new string starting at the point after the prefix, otherwise keep the string the same if the prefix is not found
if string.startswith(prefix):
    new_string = string[len(prefix):]
else:
    new_string = string

#display new string