# This code demonstrates filter funcion
a = [1,2,3,5,7,9]
b = [2,3,6,7,8,9]

print(list(filter(lambda x: x in a,b)))
print([x for x in a if x in b])