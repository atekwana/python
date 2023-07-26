# removes an element from a list
# can be stored in memory using a local variable

action_stars = ["norris", "seagal", "van dame", "me"]

action_stars.pop() # without an arg passed it will remove the last element of the list(you can save it in a variable)

print(action_stars)

print()

action_stars.pop(0)

print(action_stars)

print()

new_stars = action_stars.pop()

print(new_stars)
