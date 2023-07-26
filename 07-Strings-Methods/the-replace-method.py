# 

phone_number = "555 555 5555" 

print(phone_number.replace(" ", "-"))

print(phone_number.replace("5", "8"))

phone_number = phone_number.replace("5", "8")

phone_number = phone_number.replace(" ", "-") # strings are immutable so we override it

print(phone_number)