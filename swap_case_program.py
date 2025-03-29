#Batch 6 - Program 8
#Swap lowercase letters to uppercase and vice versa without using swapcase()

#ask the user to input a string
string = input("Enter a string: ")

#swap the cases of the characters in the string by using ASCII values
new_string = ""
for char in string:
    if "A" <= char <= "Z":
        new_string += chr(ord(char) + 32)
    elif "a" <= char <= "z":
        new_string += chr(ord(char) - 32)
    else:
        new_string += char
        
#display the new string