#Batch 7 - Program 4  
#Check if all characters in a string are lowercase without using islower()  

#ask the user to input a string
string = input("Enter a string: ")  

# Assume the string is lowercase initially  
lowercase = True  

#Check if each character in the string is lowercase by using ASCII values
for char in string:  
    if 'A' <= char <= 'Z':
        lowercase = False  
        break

# Display the result depending of the string is fully lowercase
if lowercase:  
    print("The string is fully lowercase.")  
else:  
    print("The string is not fully lowercase.")  
