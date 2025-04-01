#Batch 7 - Program 6  
#Add spaces at the beginning of a string to match an entered width without using rjust()  

#ask the user to input a string and the number of spaces to add
string = input("Enter a string: ")  
width = int(input("Enter the total width: "))  

#add the spaces at the beginning of the string 
spaces = width - len(string)  

if spaces > 0:  
    new_string = " " * spaces + string  
else:  
    new_string = string  

# Display the new string  
print(new_string)  
