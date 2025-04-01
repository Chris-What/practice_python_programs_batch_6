#Batch 6 - Program 9
#Capitalize the first letter of the string and convert the rest into lowercase without using capitalize()

#ask the user to input a string
string = input("Enter a string: ")

#capitalize the first letter of the string using ASCII values
if len(string) > 0:
    first_letter = string[0]
    if "a" <= first_letter <= "z":
        first_letter = chr(ord(first_letter) - 32)

#convert the rest of the letters into lowercase using ASCII values
    other_letters = ""
    for char in string[1:]:
        if "A" <= char <= "Z":
            other_letters += chr(ord(char) + 32)
        else:
            other_letters += char

#create and display the new string
    new_string = first_letter + other_letters
else:
    new_string = string

print(new_string)