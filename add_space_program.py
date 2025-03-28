#Batch 6 - Program 6
#Add spaces at the end of the string based on how many is wanted by the user without using ljust()

#ask the user to input a string and how many spaces they would like to add
string = input("Enter a string: ")
spaces = int(input("Enter amount of spaces to be added: "))

#add the spaces at the end of the string
if len(string) >= spaces:
    new_string = string
else:
    new_string = string + " " * (spaces - len(string))
    
#display the result