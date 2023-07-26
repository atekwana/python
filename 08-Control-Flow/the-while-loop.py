# continues to loop while the condition is true

# counter = 0

# while counter <= 5:
    
#     print(counter)
    
#     counter += 1 # must add a counter to stop the loop or else it will result in an infinite loop 
    
# print("\n", counter) # this line is not part of the loop(prints 6)

# while counter <= 5: # this loop is never reached to fix it reset counter
    
#     print(counter)
    
#     counter += 1 

# invalid_number = True

# while invalid_number:

#     user_value = int(input("please enter a number above 10: "))

#     if user_value > 10:
    
#         print(f"thanks, that works! {user_value} is a great choice!")
    
#         invalid_number = False # this will terminate the loop or else it will cause an infinite loop

#     else:
    
#         print("that doesn't fit! try again!")
    
#         # user_value = int(input("please enter a number above 10: "))  this iline is unessary for the loop


    # If the number is divisible by 3, print "Fizz" instead of the number.

    # If the number is divisible by 5, print "Buzz" instead of the number.

    # If the number is divisible by both 3 and 5, print "FizzBuzz" instead of the number.

    # If the number is not divisible by either 3 or 5, just print the number.
    
def fizzbuzz(final_number):
        
    number = 1
        
    while number <= final_number:
            
        user_input = int(input(""))
        
        if user_input % 3 == 0 and user_input % 5 == 0:
            
            print("fizzbuzz")
            
            
        
        elif user_input % 3 == 0:
            
            print("fizz")
         
            
        elif user_input % 5 == 0:
            
            print("buzz")
   
        
        else:
            
            print(f"{user_input}")
        
        number += 1
         
            

            
fizzbuzz(3)