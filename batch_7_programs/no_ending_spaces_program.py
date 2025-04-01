#Batch 7 - Program 1
#Remove spaces at the end of a string without using rstrip()

#ask user to input a string with spaces at the end
string = input("Enter a string with spaces at the end: ")

#find the last non-space character in the string and remove it
index = len(string) - 1
while index >= 0 and string[index] == ' ':
    index -= 1

new_string = string[:index + 1]

#display the new string
print(new_string)