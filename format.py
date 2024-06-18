a = float(input("float: "))

print("{0:.2f}".format(a))
print("{0:.6f}".format(a))

b = int(input("int: "))
print("{0:1d}".format(b))
print("{0:2d}".format(b))
print("{0:3d}".format(b))
print("oct:", oct(b))
print("hex:", hex(b))