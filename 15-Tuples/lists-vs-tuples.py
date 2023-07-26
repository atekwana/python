# # tuples(the immutable list)
# # the tuple itself, when it's declared, can contain mutable objects within it and those objects and the objects can be modified
birthday = (12, 7, 2000) 

# print(len(birthday))

# print(birthday[0])
# print(birthday[1])
# print(birthday[2])

# print(birthday[-1])
# print(birthday[-2])
# print(birthday[-3])

# # birthday[1] = 13 gives an error (cannot not be modified)

address = ( # immutable
    
    ["hudson street", "new york", "ny"], # this can be modified
    
    ["perrywood", "maryland", "md"]
    
)

address[1][0] = "poke street"
print(address)

print(dir(birthday))


