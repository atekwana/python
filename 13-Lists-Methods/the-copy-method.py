# shallow copy of the string (stored in the heap) objects are stored in the heap and can be reference to the stack
# the stack is used for method invocations and local variables. 
# It keeps track of method calls, method parameters, and local variables. 
# It does not store objects or their contents directly
# can be assigned to a variable()


units = ["meter", "kilogram", "second", "ampere", "kelvin", "candela", "mole"]

more_units = units.copy()

print(units)

print(more_units)

units.remove("kelvin")

even_more_units = units[:] # using slicing

print(even_more_units)



