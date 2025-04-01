#Batch 7 - Program 3  
#Convert a string to uppercase without using upper()  

#ask the user to input a string in lowercase
string = input("Enter a string in lowercase: ")  

#convert each lowercase letter to uppercase by using ASCII values
new_string = ""  
for char in string:  
    if 'a' <= char <= 'z':  # Check if the character is a lowercase letter  
        new_string += chr(ord(char) - 32)
    else:  
        new_string += char

# Display the new string  
print(new_string)  
