# differences between a variable and objects
# when we use a variable, for example, in an expression, the variable is replaced by the object that
# in python objects have data types while variables don't have a specific data type


a = 3

a = 10

a = "hello"

a = [1, 2]  # these are all a's(avoid this at all cost)

# garbage collection is the process by which the language cleans up or disposes of any leftover garbage
# the way that Python can figure that out is if they're no longer referenced by any variable, by any name, 
# those objects that no longer have references are garbage collected, which means they're
# thrown out of the computer's memory to allow for more computing power to be used for other objects that still exist in the 

a = [2, 4, 6] # a = [1, 2] is garbage collected and replaced by this new a variable


