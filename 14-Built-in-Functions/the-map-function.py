# invokes the function
numbers = [1, 2, 3, 4, 5, 6]
cubes = [index ** 3 for index in numbers] 

print(cubes)

def cube(number):
    
    return number ** 3

print(list(map(cube, numbers)))

animals = ["cat", "bear", "zebra"]

print(list(map(len, animals)))