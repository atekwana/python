# counts the number of times an element appears in a list
# case sensitive
# floating point whole numbers are the same for example 7.0 passes as 7 

car_lot = ["ford", "dodge", "acura", "acura", "chevy", "toyota"]

print(car_lot.count("acura"))
print(car_lot.count("toyota"))

print(car_lot.count("lambo"))
print(car_lot.count("Acura"))