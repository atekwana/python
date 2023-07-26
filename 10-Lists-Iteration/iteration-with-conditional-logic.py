
total = 0

random_numbers = [1, 2, 3, 4, 5]

for i in random_numbers:
    
    if i % 2 != 0: # this is the conditional statement that adds only the odd numbers in the list
        
        total += i
           
print(total) # total being outside the for loop will return only the final total instead of each iteration total

def greatest_number(numbers):
    
    greatest = numbers[0]
    
    for index in numbers:
        
        if index > greatest:
            
            greatest = index
            
    return greatest

print(greatest_number([1, 2, 3]))