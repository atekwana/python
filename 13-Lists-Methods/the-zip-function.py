# taking each element in a list and assigning it to a variable
# each element in the list represents a day f the week
# combines the list so day 1s are in the same index and so on

#             day 1    day 2     day 3
breakfast = ["eggs", "cereal", "banana"]

lunch = ["sushi", "rice", "soup"]

dinner = ["steak", "meatballs", "pasta"]


# print(zip(breakfast, lunch, dinner)) # this gives us the memory address

# print(type(zip(breakfast, lunch, dinner)))

# print(list(zip(breakfast, lunch, dinner))) # converted to a list(tuples)


for breakfast, lunch, dinner in zip(breakfast, lunch, dinner):
    
    print(f"my meal for today was {breakfast} and {lunch} and {dinner}.")
    
    



