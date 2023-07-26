# mutable objects by shared references, i mean two variables that reference the same object 
# variable links us to an object

a = 4
b = a # two variables pointing to the same object

a = 5

print(a)
print(b)

# list and dictionaries are mutable types

a = [1, 3, 5]
b = a

a.append(4)

print(a)
print(b)
