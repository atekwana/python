# an ordered data structure for declaring relationships between objects
# it's a hashmap!!!!!!!!
# a mutable data structure consisting of keys and values
# a key is object that serves as a unique identifier for a value
# a value is any python object

# keys vs values
# keys are unique, values can be duplicates
# keys must be immutable types (strings integers, floats, tuples) values can be any data type

# example
# key : value
# key : value, value, value (you can have more than one value per key)
# key : value
# and so forth

# dictionaries vs lists
# both lists and dictionaries are mutable. a dictionary can have key-value pairs added, removed or modifies
# unlike a list, a dictionary is not ordered. a dictionary is used for mappings while a list is used for order

# here we are connecting a string to string
# everything on the left is a key and the right is a value
# this is not stored in order
hashmap_for_ice_cream = { 
                         
    "benjamin": "chocolate",
    
    "kc": "cheesecake",
    
    "friend": "vanilla",
    
    "sis": "cookies and cream"
    
}

print(len(hashmap_for_ice_cream))
