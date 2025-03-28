#Batch 6 - Program 4
#Check if the string entered is fully uppercase without using isupper()

#ask the user to input a string
string = input("Enter a string: ")

#check if all characters are in uppercase by finding if a single character is lowercase, then assigning all_caps as False
all_caps = True

for char in string:
    if "a" <= char <= "z":
        all_caps = False
        break

#display the result