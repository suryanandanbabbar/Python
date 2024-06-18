# This code prints the first and second half of the string
test_str = "PythonWorld"
 
# Printing original string
print("The original string is : " + test_str)
 
# Using divmod() function
quotient, remainder = divmod(len(test_str), 2)
first_half = test_str[:quotient + remainder]
second_half = test_str[quotient + remainder:]
 
# Printing result
print("The first part of string : " + first_half)
print("The second part of string : " + second_half)