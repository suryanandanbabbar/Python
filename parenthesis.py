input_string = str(input("str: "))
nesting_level = 0
max_nesting_level = 0
valid = True

for char in input_string:
    if char == '(':
        nesting_level += 1
        if nesting_level > max_nesting_level:
            max_nesting_level = nesting_level
    elif char == ')':
        if nesting_level > 0:
            nesting_level -= 1
        else:
            valid = False
            break

if valid and nesting_level == 0:
    print(f"valid and depth: {max_nesting_level}")
else:
    print(f"not valid and errors: {max_nesting_level}")
