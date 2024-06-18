# To print Multiplication Table upto 20 rows only
x = int(input("x: "))
y = int(input("y: "))

i = 1

for i in range(1, y + 1):
    
    print("{} * {} =  {}".format(x, i, x*i))
    if i >= 20:
        print("rows is limited to 20")
        break

