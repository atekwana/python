# asterisk syntax to unpack one or more elements from a tuple into a list

employee = ("bob", "john", "manager", 50)

first_name, last_name, *details = employee # the asterisk is stored in a list(everything after two)


print(first_name, last_name, details)

*names, position, age = employee # names is stored in a list(everything before two)

print(names, position, age)

first_name, *details, age = employee # details in stored in a list(everything in the middle)

print(first_name, details, age)


