# keeps track of the index position and the element

errands = ["crank python", "pick up meds", "go to gym", "configure ssmtp"]

print(enumerate(errands)) # gives the memory address

for index, element in enumerate(errands, 1): # the second arg is for the index starting position
    
    # the index + 1 is starting at the index position 1
    print(f"{element} is number {index} on my list of thigs to do today!")