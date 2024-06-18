# Count of Vowels

# Given string (or input)
string1 = 'abracasfdaqwrteyio'

# Storing all the vowels
vowels = 'aeiouAEIOU'

# Taking empty list to store the vowels
my_list = []

# Iterating over all the characters
for i in string1:
    # Checking if the character is a vowel or not
    if i in vowels:
        # Appending the vowel character
        my_list.append(i)
    else:
        # Skip and move to next character
        pass

# Printing the length of the list or the count of the vowels
print(len(my_list)) # Output: 7


