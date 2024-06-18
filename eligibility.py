def check_eligibility(name, age):
    print("Hello", name)
    if age >= 18:
        print("You are allowed to vote")
    else:
        print("You are not allowed to vote")

# Positional Arguments
check_eligibility("Mohan", 25)

print()

# Keyword Arguments
check_eligibility(name="Mohan", age=25)