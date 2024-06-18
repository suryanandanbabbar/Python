x = int(input("x: "))
y = int(input("y: "))

if y <= 20:
    for i in range(1, y+1):
        print(f"{x} * {i} = {x*i}")
else:
    for i in range(1,21):
        print(f"{x} * {i} = {x*i}")
    print("rows are limited to 20")