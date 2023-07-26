# sorts a list in ascending number
temperatures = [40, 80, 25, 66, 35]

temperatures.sort()

print(temperatures)

temperatures.reverse()

print(temperatures)

coffees = ["latte", "espresso", "macchiato", "Frappucino"] # sorts it alphabetically based on their ascii values(capital letters are sorted before lower case letters)

coffees.sort()

print(coffees)

print(sorted(coffees)) # sorted creates a whole new object in memory

print(coffees)