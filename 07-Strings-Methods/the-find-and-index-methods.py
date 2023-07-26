# a method belongs to an object
# substring 
# if the character is not found the result will be -1

browser = "google chrome"

print(browser.find('c')) # only looks for the first appearance of c

print(browser.find("ch"))

print(browser.find('o'))

print(browser.find('g'))

print(browser.find('zxy')) # results in -1

print()

print(browser.find('o'))

print(browser.find('o', 2)) # starts from index position 2

print(browser.rfind('o', 5)) # starts from index position 5

print()

print("ch" in browser)

#print(browser.index('c')) # index raises a value error if it's not found

#print(browser.index('z'))


