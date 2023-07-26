# number of times a character appears in a string

word = "queueing"

print(word.count('e'))

print(word.count('u'))

print(word.count('q'))

print(word.count('z'))

print(word.count('Q'))

print(word.count("ue")) # must be next to each other or else it will result in 0

print(word.count("ing")) # must be next to each other or else it will result in 0

print(word.count('u') + word.count('e')) # add boths occurances

