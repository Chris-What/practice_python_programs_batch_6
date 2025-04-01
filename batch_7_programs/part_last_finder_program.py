#Batch 7 - Program 10  
#Find the last location of a part the user inputs in a string without using rindex()  

#ask the user to input a string and a part they want to find 
string = input("Enter a string: ")  
part = input("Enter the part to find: ")  
  
#initialize a variable to store the index  
found_part = -1  

#loop through the string in reverse to find the last location of the part  
part_length = len(part)  

for i in range(len(string) - part_length, -1, -1):  
    if string[i:i + part_length] == part: 
        found_part = i  
        break

#display the result  
if found_part != -1:  
    print(f"The part last appears at index {found_part}.")  
else:  
    print("The part was not found in the string.")  
