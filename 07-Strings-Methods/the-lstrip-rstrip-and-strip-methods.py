# for data formatting and cleaning up

empty_space = "             content             "

print(empty_space.rstrip()) # right side strip

print(len(empty_space.rstrip()))

print(empty_space.lstrip())

print(len(empty_space.lstrip()))

print(empty_space.strip()) # clears all white space

website = "www.python.org"

print(website.lstrip('w'))

print(website.rstrip('org'))

print(website.strip("worg.")) # both begenning and end

string = "       geronimo crikey  "

print(string.strip().replace("g","z").replace(" ", "!"))
