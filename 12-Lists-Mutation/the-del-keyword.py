# deletes the element and does not store it in memory like pop
# works with negative numbers as well

soups = ["french onion", "clam chowder", "chciken noodle", "miso", "woton"]

del soups[0] # cannot be stored in a variable

print(soups)

del soups[1 : 3] # removes more than one element from the list

print(soups)

