# returns true if all the elements in the iterable object is true
# all the elements must be true

print(all([True]))
print(all([True, False]))
print(all([1, 2, 3]))
print(all([1, 3, 0]))
print(all(['a', 'b']))
print(all(['b', 'b', '']))

print(all([True, False]))
print(all([False, False]))
print(all([0, 1]))
print(all([0]))
print(all(['', ' ']))
print(all(['']))

print(all([]))

