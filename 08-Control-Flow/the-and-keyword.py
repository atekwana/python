if 5 < 7 and "rain" == "rain": # both conditions must be true so the print statement will execute
    
    print("both conditions are true")
    
if 5 < 7 and "rain" == "fire": # only one conditon is true so the statement won't print
    
    print("this will not print")

if "rain" == "fire" and 5 < 7: # because the first condition is false, it automatically doesn't print

    print("this will not print")
    
# great for numerical ranges

value = 95

#if value > 90 and value < 100:

if 90 < value < 100:
    
    print("this is a shortcut")