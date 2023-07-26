# define a function that iterates over a list of numbers,
# gets the product of each numbe by one less than its index position
# and returns the total sum of those products

'''
visualizing the code

values = [1, 2, 3, 4]
1 * (0 - 1) = -1 
2 * (1 - 1) = 0
3 * (2 - 1) = 6
4 * (3 - 1) = 8
===============
sum           25

'''

values = [1, 2, 3, 4]

def product(list):
    
    total = 0
    
    for index, element in enumerate(list):
        
        total += element * (index - 1)
    
    return total

print(product(values))