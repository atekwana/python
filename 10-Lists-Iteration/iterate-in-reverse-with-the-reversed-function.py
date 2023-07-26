
random_names = ["me", "you", "they", "we"]

for character in random_names[::-1]:
    
    print(f"{character} has a total of {len(character)} characters.")
    
    
print(reversed(random_names))

print(type(reversed(random_names)))