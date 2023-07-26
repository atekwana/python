# the continue button moves where ever the break point is that is where the programm stops 
# the step over button moves through the line without a break point (staying in the current scope) 
# variable at any point of execution. if there's a break point it will pause on the break point(forces us into another scope)
# step into steps into a lower level scope()
# step out returns back to the higher level scope

print("welcome to my program") # whereever the break point is that is where the programm stops 

def fun_stuff():
    
    a = 20
    
    print("hello")
    
    print("goodbye")
    
    a = 25
    
    return a

final_value = fun_stuff()

print(fun_stuff())