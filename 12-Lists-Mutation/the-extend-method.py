# similar to append in java
# adding to the end of a list
# extend  method takes one or multiple args & adds to a list usually at the end of a list

mountains = ["mount everest", "idk"]

print(mountains)

mountains.extend(["kilamajaro", "makalu", "bowie"])

more_mountains = ["idk", "more mountains"]

mountains.extend(more_mountains)

print(mountains)

steaks = ["tenderloin", "new york strip"]

more_steaks = ["t-bone", "another steak"]

my_meal = steaks + more_steaks

print(my_meal)

print(steaks)

print(more_steaks)

