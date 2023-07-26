import copy
# # a shallow copy, a shallow copy creates a new list and it inserts references into it.

# # For all the objects found in the original list, shallow copying is a great choice if the original list

# # does not contain any nested lists.

# # There are three ways that we can create a shallow copy with lists, slicing syntax with the copy method

# # or with a copy function from the copy module.

# a = [1, 3, 4]

# b = a[:]

# print(a == b)
# print(a is b)

# print()
# c = a.copy()
# print(a == c)
# print(a is c)

# print()
# d = copy.copy(a) # a is equal to d but not identical to d
# print(a == d)
# print(a is d)

numbers = [1, 2, 4] 
a = [1, numbers, 5]

b = a[:] # shallow copies
b = a.copy()
b = copy.copy(a)
b = copy.deepcopy(a) # deep copy, copies everything about a
print(a[1] is b[1])

print()
a[1].append(100)
print(b)
print(a)

print()
b[1].append(200)
print(b)
print(a)

# deep copy, which goes as many levels down as you need to.