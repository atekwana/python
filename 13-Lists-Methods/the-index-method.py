# location of a given element in a list( first occurance)
# error if the element is not in the list(can be bypassed using a conditional if statement)

pizzas = ["mushroom", "pep", "sausage", "pep", "chicken", "sausage"]

print(pizzas.index("chicken"))
print(pizzas.index("pep"))
print(pizzas.index("sausage"))

if "olives" in pizzas:
    
    print(pizzas.index("olives"))
    
# you can start the search from a specific index
print(pizzas.index("pep", 2))
print(pizzas.index("sausage", 3)) # starting value is inclusive