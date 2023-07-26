# # only removes the first occurance of the element in the list

# nintendo_games = ["zelda", "mario", "donkey kong", "zelda"]

# nintendo_games.remove("zelda")

# print(nintendo_games)

# if "wario" in nintendo_games:
    
#     nintendo_games.remove("wario")
    
# if "mario" in nintendo_games: # with this condition, one can remove all occurances of an element in a list
    
#     nintendo_games.remove("mario")

# print(nintendo_games)

def delete_all(string_list, target):
    
    while target in string_list:
            
        string_list.remove(target)
            
    return string_list

print(delete_all([4, 4, 4], 4))