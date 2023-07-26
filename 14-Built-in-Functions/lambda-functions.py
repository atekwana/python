# an anonymous function( a function without a name)

metals = ["gold", "platnium", "silver", "palladium"]
#                              implicit return value
print(list(filter(lambda index: len(index) > 5, metals)))

print(list(filter(lambda index: 's' in index, metals))) # return all elements with p

print(list(map(lambda index: index.count('l'), metals)))

print(list(map(lambda index: index.replace('s', '$'), metals)))

def right_words(list_words, number):
    
    return list(filter(lambda index: len(index) == number, list_words))

print(right_words(['cat', 'dog', 'bean', 'ace', 'heart'], 3))