# accepts a numeric value as an arg and a string
# second arg is the format specifier
# always return a string( it is used for aesthetic purposes)

number = 0.123456789

print(format(number, "f"))

print(format(number, ".2f")) # only two decimal places

print(format(0.5, ".2%"))