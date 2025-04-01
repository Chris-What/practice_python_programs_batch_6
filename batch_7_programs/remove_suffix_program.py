#Batch 7 - Program 2  
# emove a specified suffix from a string without using removesuffix()  

#ask the user to input a string  and a suffix to remove
string = input("Enter a string: ")  
suffix = input("Enter the suffix to remove: ")  

#check if the string ends with the suffix and remove it  
if string.endswith(suffix):  
    new_string = string[:-len(suffix)]  
else:  
    new_string = string  

#display the new string  
print(new_string)