# 2d arrays in java

bubble_tea_flavours = [  # outer list has 3 element
    ["honeydew", "mango", "passion fruit"], # nested list contains 3 elements 
    ["peach", "plum", "strawberry", "taro"], # nested list contains 4 elements 
    ["kiwi", "chocolate"] # nested list contains 2 elements 
]

# print(len(bubble_tea_flavours))

# print(bubble_tea_flavours[0]) # this seperates each nested list
# print(bubble_tea_flavours[1])
# print(bubble_tea_flavours[2])

# print(len(bubble_tea_flavours[0]))
# print(len(bubble_tea_flavours[1]))
# print(len(bubble_tea_flavours[2]))

# accessing an element from a specific nested list
# first is extract the nested list
# second is extract the index position
# like a 2d array in java [nested_list][index_postion_of_the_element_inside_the_nested_loop]                       
print(bubble_tea_flavours[1][2])
print(bubble_tea_flavours[0][0])

all_flavours = []

for index in bubble_tea_flavours: # looping through a nested list
    
    for flavour in index:
        
        all_flavours.append(flavour)
        
print(all_flavours)

def draw_star_pattern(rows):
    for i in range(rows):
        for j in range(i + 1):
            print("*", end=" ")
        print()

# Example usage
rows = 5
draw_star_pattern(rows)

    