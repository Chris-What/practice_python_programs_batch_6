#Batch 7 - Program 5  
#Check if a string starts with the  prefix without using startswith()  

#ask the user to input a string and a prefix they want to check
string = input("Enter a string: ")  
prefix = input("Enter the prefix to check: ")  

#check if the string starts with the prefix
prefix_check = True  

if len(prefix) > len(string):  
    prefix_check = False
else:  
    for i in range(len(prefix)):  
        if string[i] != prefix[i]:
            prefix_check = False  

# Display the result  
if prefix_check:  
    print("The string starts with the entered prefix.")  
else:  
    print("The string does not start with the entered prefix.")  
