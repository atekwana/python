# creates a list from something else

numbers = [3, 4, 5, 6, 7]

# new_list = []

# for index in numbers:
    
#     new_list.append(index ** 2)
    
# print(new_list)

# print(index)

squares = [index ** 2 for index in numbers] # simpler method 

print(squares)

rivers = ["nile", "amazon", "yanzu"]

print([len(index) for index in rivers]) # length of each string in the list

rivers = ["nile", "amazon", "yanzu"]

print([index.upper() for index in rivers]) # prints each river in uppercase

decimals = [3.4, 5.6, 8.8]

print([int(index) for index in decimals])
