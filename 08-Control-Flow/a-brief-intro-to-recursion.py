# keeping in mind different dimensions in code
# when a function calls itself

# def count_down_from(number):
    
#     start = number
    
#     while start > 0: # this does not use recursion
        
#         print(start)
        
#         start -= 1 # loop control(helps ends the loop)

def count_down_from(number):
    
    if number <= 0: # base case(for recursive control(stopping the recursive function))
        
        return number
    
    else:
        
        print(number)
        
        return count_down_from(number - 1) # recursive case

count_down_from(5)   
    