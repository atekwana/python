# similar to append in java when it comes to adding chars(think belasso cipher) using string builder
# instead of using += 
# because list is an object

powerball_numbers = [4, 8, 15, 23, 42]

def squares(numbers):
    
    new_numbers = []
    
    for index, element in enumerate(powerball_numbers):
        
        new_numbers.append(element * element)

    return new_numbers


print(squares(powerball_numbers))

def convert_to_float(numbers):
    
    floats = []
    
    for index in numbers:
        
        floats.append(float(index))
        
    return floats

print(convert_to_float(powerball_numbers))


def even_or_odd(numbers):
    
    result = []
    
    for index in numbers:
        
        if index % 2 == 0:
            
            result.append(True)
            
        else:
            
            result.append(False)
            
    return result

print(even_or_odd(powerball_numbers))