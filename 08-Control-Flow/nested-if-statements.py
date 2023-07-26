ingridient = "pasta"

meat = "meatballs"

if ingridient == "pasta":
    
    if meat == "meatballs":
        
        print("you should make pasta")
        
    else:
        
        print("i recommend making plain pasta")
        
else:
    
    print("i have no recommendations")
    
# better way for me currently

if ingridient == "pasta" and meat == "meatballs":
    
    print("i recommend making pasta and meatballs")

elif ingridient == "pasta":
    
    print("make plain pasta")
    
else:
    
    print("i have no recommendations")
    
    