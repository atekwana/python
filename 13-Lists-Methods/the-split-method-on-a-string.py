# used for string objects
# this accepts a list 
# complementary to the join method
# make sure to always store in a variable for reusing purposes

users = "bob, jon, sue, randy"

print(users.split(", ")) # two args have been passed

print(users.split(", ", 2)) # eve

sentence = "i am learning to code"

words = sentence.split(" ") # must be not an string

print(words)


