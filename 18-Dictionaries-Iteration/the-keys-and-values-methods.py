'''
a dictionaries, keys or values one element at a time, 
both methods return and iterable dictionary

'''

cryptocurrency_prices = {
    
    "bitcoin": 400,
    
    "litecoin": 700,
    
    "dodgecoin": 100
}

print(cryptocurrency_prices.keys()) # getting keys only

print(cryptocurrency_prices.values()) # getting values only

# preffered logic
for key in cryptocurrency_prices.keys():
    
    print(f"the next currency is {key}")
    
for value in cryptocurrency_prices.values():
    
    print(f"the next price is {value}")
    

