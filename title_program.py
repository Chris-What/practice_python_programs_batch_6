#Batch 6 - Program 10
#Capitalize the first letter of every word in the string and convert every other letter into lowercase without using title()

#ask the user to input a string
string = input("Enter a string: ")

#split the words in the string and store every changed word
words = string.split(" ")
new_words = []

#capitalize the first letter of every word by using ASCII values
for word in words:
    if len(word) > 0:
        first_letter = []
        if "a" <= first_letter <= "z":
            first_letter = chr(ord(first_letter) - 32)

#convert every other letter into lowercase by using ASCII values
        other_letters = ""
        for char in words[1:]:
            if "A" <= char <= "Z":
                other_letters += chr(ord(char) + 32)
            else:
                other_letters += char

#display the new string