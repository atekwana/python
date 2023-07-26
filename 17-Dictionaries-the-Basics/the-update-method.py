'''
In this lesson, we'll take a look at the update method, 
which merges one dictionary into another.

if the key pairs are the same, the mutating method will the dictionary the method is invoked upon 
in this scenario, employee_salaries. while extra.. will override it

'''

employee_salaries = {
    
    "kc": 100000,
    
    "james": 50000,
    
    "yugi": 1334534
}
extra_employee_salaries = {
    
    "jenny": 1003453,
    
    "kc": 500111,
    
    "madison": 240280
    
}

employee_salaries.update(extra_employee_salaries) # this can be reversed

print(employee_salaries)

print(extra_employee_salaries)

