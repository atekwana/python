#print("organic"[5])

web_browers = ["chrome", "edge", "firefox"]

print(web_browers[0]) # index position of 0 (chrome)

print(web_browers[- 1])

for i in web_browers: # printin all elements in the list in order
    
    print(i)
    
#print(web_browers[10]) index out of bounds error
print(web_browers[2][3]) # first [goes into the third element of the list] and second[goes into the third index character in the string]

presidents = ["washington", "adams", "jefferson"]

print(presidents[-1])
print(presidents[-2])
print(presidents[-3])

# print(presidents[-20]) index out of range 