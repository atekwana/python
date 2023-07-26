# any number of positional arguments using an * (it creates a tuple)

def accept_stuff(*args): # collect any number of positional arguments when the function is called(don't forget the *)
    
    print(type(args))
    print(args)

accept_stuff(1)
accept_stuff(1, 2, 3, 4, 5, 6)
accept_stuff()

def my_max(*numbers, random):
    
    print(random)
    
    greatest = numbers[0]
    
    for index in numbers:
        
        if index > greatest:
            
            greatest = index
            
    return greatest

print(my_max(1,3, 4, random = "shazam"))
print(my_max( 1, 5, 10, random = "horay"))
print(my_max( -5, -4, random = "don't"))

# in reserve 

        
        
