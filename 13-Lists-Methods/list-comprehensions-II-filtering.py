# extracting a subset of elements from an original iterable

# list comprehension from a string

print(["abcdefghijklmnopqrstuvwxyz".index(index) for index in "donut"])

print([index / 2 for index in range(20)]) # dividing

donuts = [
    "boston cream",
    "jelly",
    "vanilla cream",
    "glazed",
    "chocolate cream"
]

# creamy_donuts = []

# for index in donuts:
    
#     if "cream" in index:
        
#         creamy_donuts.append(index)
        
# print(creamy_donuts)

creamy_donuts = [index for index in donuts  if "cream" in index] # simplified version using list comprehension

print(creamy_donuts)

print(len([index for index in donuts  if "cream" in index]))

print([index.split(" ")[0] for index in donuts  if "cream" in index])


