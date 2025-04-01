#Batch 7 - Program 9  
#Find the first location of a part the user inputs in a string without using index()  

#ask the user to input a string and the part they want to find
string = input("Enter a string: ")  
part = input("Enter the part to find: ")  

#initialize a variable to store the index  
found_part = -1  

#loop through the string to find the first location of the part  
part_length = len(part)  

for i in range(len(string) - part_length + 1):  
    if string[i:i + part_length] == part:
        found_part = i  
        break

# Display the location of the part  
if found_part != -1:  
    print(f"The part first appears at index {found_part}.")  
else:  
    print("The part was not found in the string.")  