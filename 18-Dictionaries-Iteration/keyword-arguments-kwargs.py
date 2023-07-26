# bundles key word arguments into a dictionary

def length(word):
    
    return len(word)

print(length("hello"))

print(length(word= "hello"))

# going to represent a dictionary
# keep in mind that "kwargs" uses two "**"
def collect_keyword_args(**kwargs):
    
    print(kwargs)
    
    for key, value in kwargs.items():
        
        print(f"the key is {key} and the value is {value}")

collect_keyword_args(a = 2, b = 3, c = 4)


# keep in mind that "args" uses one "*"
# keep in mind that "*args" must come first before "**kwargs"
def args_and_kwargs(a, b, *args, **kwargs):
    
    print(f"the total of your regular args a and b is {a + b}")
    
    print(f"the total of your args tuple is {sum(args)}")
    
    # getting the total of values in the dictionary
    
    total = 0
    
    for value in kwargs.values():
        
        total += value
        
    print(f"the total of your kwargs dictionary is {total}")
    
args_and_kwargs(1, 2, 3, 4, 5, y = 10)
    
    