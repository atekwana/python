# forces the loop to move to the iteration immediately(current iteration)
# usually in an if statement

# def sum_of_positive_numbers(values): # with out continue
    
#     total = 0
    
#     for value in values:
        
#         if value > 0:
            
#             total += value
    
#     return total

def sum_of_positive_numbers(values):
    
    total = 0
    
    for value in values:
        
        if value < 0:
            
            continue
        
        total += value # this line will only be reached if the value is greater than 0
        
    return total
    

print(sum_of_positive_numbers([1, 2, -3, 4]))
