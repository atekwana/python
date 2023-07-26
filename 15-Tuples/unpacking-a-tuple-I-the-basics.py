# A tuple object can be unpacked, which means we can assign its ordered elements into multiple variables

employee = ("bob", "john", "manager", 50)

# first_name = employee[0] # long way

# last_name = employee[1]

# position = employee[2]

# age = employee[3]


# first_name, last_name, position, age = employee # unpacking the tuple

# print(first_name, last_name, position, age)

# subject, verb, adjective = ["python", "is", "fun"]

# print(subject, verb, adjective)

# last_name, position, age = employee # error not enough variables

# first_name, last_name, position, age, salary = employee # error more than enough variables

a = 5

b = 6
#      this happens first "a, b"
b, a = a, b


print(a, b)


