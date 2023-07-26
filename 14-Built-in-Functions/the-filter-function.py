# returns true or false
# instead of list comprehension
animals = ["animals", "horse", "cat", "giraffe", "cheetah", "dog"]

long_words = [index for index in animals if len(index) > 5]

print(long_words)

def is_long_animal(index): 
    
    return len(index) > 5

print(list(filter(is_long_animal, animals)))
    
