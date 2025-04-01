#Batch 7 - Program 8  
#Count how many times the part the user inputs appears in a string without using count()  

#ask the user to input a string and a part they want to count
string = input("Enter a string: ")  
part = input("Enter the substring to count: ")  

#Initialize a counter for how many times the part will appear in the string
count = 0  

#go through the string and check how many times the part appears
part_length = len(part)  

for i in range(len(string) - part_length + 1):  
    if string[i:i + part_length] == part:  # Compare slices  
        count += 1  

#display the count  
print(f"The part {part} appears {count} times in the string.")  
