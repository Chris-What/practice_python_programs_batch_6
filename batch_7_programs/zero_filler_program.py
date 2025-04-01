#Batch 7 - Program 7  
#Add zeros at the beginning of a string according to the user input of zeros without using zfill()  

# Ask the user to input a string  and how long the zeros will be
string = input("Enter a string: ")  
width = int(input("Enter the total width of the string: "))  

#chcek how many zeros are need
zeros = width - len(string)  

if zeros > 0:  
    new_string = "0" * zeros + string  
else:  
    new_string = string  

# Display the new string  
print(new_string)  
