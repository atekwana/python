# two or more characters is extracted through slicing

address = "attractive street, beverly hills, CA 20878"

print(address[0 : 3]) # the value of 0 is inclusive and the value of 3 is excluded

print(address[0 : 4]) # the value of 0 is inclusive and the value of 4 is excluded

print(address[0 : 17]) # the value of 0 is inclusive and the value of 17 is excluded

print(address[19 : 32]) # left is included and right is excluded

print(address[19 : 100]) # no error because the right is infinity

print()

print(address[34 : -6])

print(address[-8 : -6])

print(address[-8 : 36])

print()

print(address[0 :]) # 0 to infinity

print(address[10 :]) # 0 to infinity

print(address[: 10]) # 0 to 10 noninclusive

print(address[: -3]) # leaves out the last three characters

print()

print(address[:]) # this copies the string object

