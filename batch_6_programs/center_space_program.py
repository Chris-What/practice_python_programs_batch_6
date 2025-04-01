#Batch 6 - Program 7
#Center the string with spaces without using center()

#ask the user to input a string and how many spaces would they like to add
string = input("Enter a string: ")
spaces = int(input("Enter amount of spaces to be added: "))

#add the spaces to the left and right of the string by evenly distributing them to each side to ensure the string is in the center
if len(string) >= spaces:
    new_string = string
else:
    total_spaces = spaces - len(string)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

#create and display a new string centered within the spaces by adding all the new variables together
new_string = " " * left_spaces + string + " " * right_spaces

print(new_string)