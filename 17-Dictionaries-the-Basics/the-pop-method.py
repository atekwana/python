# year = [2000, 2001, 2002, 2003]

# year.pop() # no argunent removes the last element added to the list(can be stored in a local variable)

# print(year)

# year.pop(0) # this removes the element at index 0

# print(year)


release_dates = {
    
    "python": 1991,
    
    "ruby": 1995,
    
    "java": 1995,
    
    "go": 2007
}

year = release_dates.pop("java")
print(release_dates)
print()

print(year)
print()

release_dates.pop("go")
print(release_dates)
print()

if "rust" in release_dates: 
    
    release_dates.pop("rust")
    
    
new_year = release_dates.pop("c++", 2000) # with a second arg, if the key does not exist it will print the new value
print(new_year)

print()
# keep in mind that if you provide a value for an existing key, then the original value is printed
another_year = release_dates.pop("ruby", 2000)
print(another_year)

# using delete
del release_dates["python"]
print(release_dates)