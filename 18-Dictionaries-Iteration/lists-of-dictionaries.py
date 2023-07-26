# a complex data structure
# 
# 
# 

concert_attendees = [
    
    {"name": "taylor", "section": 400, "price paid": 99.99},
    
    {"name": "taylor", "section": 3, "price paid": 499.99},
    
    {"name": "taylor", "section": 1, "price paid": 0.0}
    
]

for attendee in concert_attendees:
    
    for key, value in attendee.items():
        
        print(f"the {key} is {value}")
