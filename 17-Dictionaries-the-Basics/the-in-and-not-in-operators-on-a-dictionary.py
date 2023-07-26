
pokemon = {
    
    "fire": ["charmader", "charmeleon", "charizard"],
    
    "water": ["squirtle", "warturtle", "blastoise"],
    
    "grass": ["bulbasaur", "venusaur", "ivysaur"]
      
}

# watch out for case sensitivity
print("fire" in pokemon)
print("electric" in pokemon)

print("electric" not in pokemon)

if "zombie" in pokemon:
    
    print(pokemon["zombie"])

else:
    
    print("the category of zombie does not exist")



