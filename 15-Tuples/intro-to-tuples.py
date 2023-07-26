# a fixed length immutable list
# cannot be modified or change once created
# the comma makes it a tuple (so two or more elements)

foods = "sushi", "steak", "guac"

foods = ("sushi", "steak", "guac") # best practice 

print(type(foods))

empty_tuple = ()

print(type(empty_tuple))

mystery = (1, ) 

print(type(mystery))

print(tuple(["sushi", "steak", "guac"])) 

print(tuple("abc"))

faves = ["great gatsby", "iron man", "logan"]
print(tuple([faves]))


