#Batch 6 - Program 5
#Check if the string ends with the entered suffix without using endswith()

#ask the user to input a string and the suffix they want to check
string = input("Enter a string: ")
suffix = input("Enter suffix you want to check: ")

#check if the end of the string matches with the suffix by comparing them
if len(suffix) > len(string):
    suffix_check = False
else:
    suffix_check = (string[-len(suffix):] == suffix)

#display the result depending if the suffix matches the end of the string or not
if suffix_check:
    print("The string ends with the entered suffix.")
else:
    print("The string does not end with the entered suffix.")