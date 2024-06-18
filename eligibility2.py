def check_eligibility(name, age, gender):
    print("Hello", name)
    print("Gender:", gender)
    if age < 18:
        print("Not Allowed to Vote.")
    elif age > 90:
        print("You are too old, vintage piece; we don't want your vote. Better stay at home.")
    else:
        print("Allowed to Vote.")

check_eligibility(name=input("Name: "), gender=input("Gender: "), age=int(input("Age: ")))