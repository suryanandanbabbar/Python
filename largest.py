# This code finds out the largest of three user-given numbers.

# Take inputs from the user as a single line separated by spaces
a, b, c = map(float, input("Enter three numbers (a b c): ").split())

# Find the largest number
largest = max(a, b, c)

# Print the result
print(f"The largest number is: {largest}")

# Using Fruitful function (return function)
def largest(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b    
    else:
        return c

result = largest(a,b,c)
print("Using function, largest number:", result)