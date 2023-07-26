
string = "winter"

print(string.islower())

string = string.title()

print(string.islower())

print(string.istitle())

print(string.isupper())

string = string.upper()

print(string.isupper())

print(string.isalpha()) # checks if it's alphabetic

string = "area 51"

print(string.isalpha()) # checks if it's alphabetic

print(string.isnumeric()) # checks if it's numeric

print(string.isalnum()) # checks if it's alphabetic or numeric (a space will affect the ouput)

string = " "

print(string.isspace()) # must be entirely a space

string = "morning awaits"

print(string.capitalize())
