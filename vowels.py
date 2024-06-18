while True:
    user_input = input("Enter a character (-1 to quit): ")

    if user_input == '-1':
        print("Program terminated.")
        break

    if user_input in 'aeiouAEIOU':
        print(f"{user_input} is a vowel.")
    elif len(user_input) == 1 and user_input.isalpha():
        print(f"{user_input} is not a vowel.")
    else:
        print("Invalid input. Please enter a single alphabet character.")
