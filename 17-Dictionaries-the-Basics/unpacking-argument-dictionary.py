'''
take a look at how a dictionary can be transformed into keyword arguments.
it's a process called unpacking, very similar to how a tuple or a list can be unpacked.

how a dictionary can be transformed into keyword arguments.

'''

def height_to_meters(feet, inches):
    
    total_inches = (feet * 12) + 12
    
    return total_inches * 0.0254
    
print(height_to_meters(5, 9))

stats = {
    
    "feet": 5,
    
    "inches": 9
    
}

print(height_to_meters(**stats))