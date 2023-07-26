# the order is not gauranteed
# use to establish key value pairs

# ANTI-PATTERN 
# a solution to a programming problem that is considered ineffective or counter-productive

chinese_food = {
    
    "noodles": 9.99,
    
    "fried rice": 8.99,
    
    "wings": 1.99
    
}

for food in chinese_food:
    
    print(f"the food is {food} and its price is {chinese_food[food]}")
    
    
    
pounds_to_kilograms = {

    5: 2.267678,
    
    10: 4.53592,
    
    25: 11.3398
}

for pound in pounds_to_kilograms:
    
    print(f"the pound is {pound} and its matching kilogram is {pounds_to_kilograms[pound]} kilograms")
    
'''
HashMap<Integer, Integer> pound = new HashMap<Integer, Integer>();

for (Integer key : pound.keyset()) {
    
    System.out.println("key = " + key);
    
} // vice versa for the the values only ("pound.values()")

'''