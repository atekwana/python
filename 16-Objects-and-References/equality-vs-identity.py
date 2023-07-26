# two objects are equal, whether they have the same values or structure or shape in comparison identity

# checks, if two names in the program point to the actual same object, the same object in your computer's memory.

students = ['a', 'b', 'c']

athletes = students

nerds = ['a', 'b', 'c']


print(students == athletes)
print(students == nerds)

print()

print(students is athletes)
print(students is nerds)

a = 1
b = 1 # both a and b reference the same object in memory

print(a == b)
print(a is b)



