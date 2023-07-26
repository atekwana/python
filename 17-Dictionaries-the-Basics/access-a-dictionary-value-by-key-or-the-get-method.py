hashmap_for_flight_prices = {
    
    "chicago": 99,
    
    "san francisco": 130,
    
    "new york": 50
    
}


print(hashmap_for_flight_prices["chicago"])
print(hashmap_for_flight_prices["san francisco"])
print(hashmap_for_flight_prices["new york"])

# print(hashmap_for_flight_prices["boston"]) key error because the key does not exist

gym_membership_packages = {
    
    29: ["machines"],
    
    49: ["machines", "vitamins"],
    
    79: ["machines", "vitamins", "sauna"]
    
}

print(gym_membership_packages[29])
print(gym_membership_packages[79])
# print(gym_membership_packages[100])

# access a value by the key through get(key, default value to return only if the key is not found in the dictionary)
print(gym_membership_packages.get(29, ["basic dumbells"]))

print(gym_membership_packages.get(100, ["too expensive"]))

print(gym_membership_packages.get(100))

