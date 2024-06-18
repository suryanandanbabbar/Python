def remove_digits(input_string):
    result = ''.join(char for char in input_string if not char.isdigit())
    return result

input_string = input("str: ")
output_string = remove_digits(input_string)

print(output_string)