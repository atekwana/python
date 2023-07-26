# break is usually associated with an if statement inside a for loop

print(3 in [1, 2, 3, 4, 5, 3]) # no point in iterating after 3 is found in this scenario


def contains(values = int, target = int):
    
    found = False
    
    for value in values:
        
        print(value)
        
        if value == target:
            
            found = True
            
            break # stops the loop when the value is found(must be in the if statement)
        
    return found

print(contains([1, 2, 3, 4, 5, 6], 3))