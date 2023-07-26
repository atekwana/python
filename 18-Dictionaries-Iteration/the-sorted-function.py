numbers = [4, 68, 45, 9]

print(sorted(numbers))

salary = {
    
    "ceo": 100,
    
    "onwer": 4000
}

print(sorted(salary))

# getting only keys and values
print(sorted(salary.keys()))
print(sorted(salary.values()))

wheel_count = {
    
    "bike": 2,
    
    "car": 4,
    
    "bus": 8
}

for vehicle, count in sorted(wheel_count.items()):
    
    print(f"the next vehicle is a {vehicle} and it has {count} wheels")