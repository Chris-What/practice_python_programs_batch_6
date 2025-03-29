#Batch 6 - Program 10
#Capitalize the first letter of every word in the string and convert every other letter into lowercase without using title()

#ask the user to input a string
string = input("Enter a string: ")

#split the words in the string and store every changed word
word = string.split(" ")
new_words = []

#capitalize the first letter of every word
#convert every other letter into lowercase
#display the new string