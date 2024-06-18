# This code demonstrates squares of numbers in a list
def squares(x):
    return x ** 2

list1 = list(map(int, input().split(",")))
result = map(squares, list1)

# Normal Way
print("Normal Way")
print(list(result))

# Using anonmyous function i.e. lambda function
print("Using lamda function")
print(list(map(lambda x: x **2,list1)))

# Using list comprehension
print("Using list comprehension")
print([x**2 for x in list1])