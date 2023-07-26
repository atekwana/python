# fibonacci sequence

def reverse(string):
    
    if len(string) <= 1: # base case
        
        return string
    
    else: 
        
        return string[-1] + reverse(string[:-1])
    
print(reverse("straw"))