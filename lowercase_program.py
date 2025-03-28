#Batch 6 - Program 3
#Convert a string into lowercase without using lower()

#ask the user to input a string with uppercase letters
string = input("Enter a string with uppercase letters: ")

#convert the uppercase letters in the string into lowercase by using ASCII values
new_string = ""
for char in string:
    if "A" <= char <= "Z":
        new_string += chr(ord(char) + 32)
    else:
        new_string += char

#display the new string
print(new_string)