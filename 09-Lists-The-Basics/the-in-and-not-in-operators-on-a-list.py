print("fast" in "breakfast")

print("fast" in "dinner")

meals = ["breakfast", "lunch", "dinner"]

print("lunch" in meals) # case sensitive

print("dinner" in meals)
 
print("snack" in meals)

print()

test_scores = [99.0, 35.9, 25.5]

print(99.0 in test_scores)

print(60.0 in test_scores)

print(35.9 in test_scores)

print(25.5 in test_scores)

print()

print("lunch" not in meals and 99.0 in test_scores)

print("Breakfast" not in meals)

if 1000 not in test_scores:
    
    print("not in there")



