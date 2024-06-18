def check_matching_parentheses(input_string):
    nesting_level = 0
    max_nesting_level = 0
    error_positions = []

    for i, char in enumerate(input_string):
        if char == '(':
            nesting_level += 1
            max_nesting_level = max(max_nesting_level, nesting_level)
        elif char == ')':
            if nesting_level > 0:
                nesting_level -= 1
            else:
                error_positions.append(i)

    error_positions.extend(range(len(input_string) - nesting_level, len(input_string)))

    if not error_positions:
        print(f"str: {input_string}")
        print(f"valid and depth: {max_nesting_level}")
    else:
        print(f"str: {input_string}")
        print(f"not valid and errors: {len(error_positions)}")

# Example usage:
input_string = input("Enter a string with parentheses: ")
check_matching_parentheses(input_string)
