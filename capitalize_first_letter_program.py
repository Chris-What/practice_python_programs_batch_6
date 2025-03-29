#Batch 6 - Program 9
#Capitalize the first letter of the string and convert the rest into lowercase without using capitalize()

#ask the user to input a string
string = input("Enter a string: ")

#capitalize the first letter of the string using ASCII values
if len(string) > 0:
    first_letter = string[0]
    if "a" <= first_letter <= "z":
        first_letter = chr(ord(first_letter) - 32)

#display the new string