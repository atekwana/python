def positive_or_negative(number):
    
    if number > 0:
        
        return "postive number"
        
    elif number < 0:
        
        return "negative number"
        
    else:
        
        return "neither"
    
print(positive_or_negative(4))   
print(positive_or_negative(-3))   
print(positive_or_negative(0)) 

def calculator(operation, a, b):
    
    if operation == "add":
        
        return a + b
    
    elif operation == "substraction":
        
        return a - b
    
    elif operation == "multiply":
        
        return a * b
    
    elif operation == "divide":
        
        return a / b
    
    else:
        
        return "pick an option please"
        
print(calculator("add", 3, 4))
print(calculator("substraction", 3, 4))
print(calculator("multiply", 3, 4))
print(calculator("divide", 3, 4))
print(calculator("gibberish", 3, 4))
    