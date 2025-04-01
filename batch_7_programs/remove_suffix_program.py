# Batch 7 - Program 2  
# Remove a specified suffix from a string without using removesuffix()  

# Ask the user to input a string  and a suffix to remove
string = input("Enter a string: ")  
suffix = input("Enter the suffix to remove: ")  

# Check if the string ends with the suffix and remove it  
if string.endswith(suffix):  
    new_string = string[:-len(suffix)]  
else:  
    new_string = string  

# Display the new string  
print(new_string)