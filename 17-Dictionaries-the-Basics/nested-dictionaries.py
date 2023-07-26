'''
a key in a dictionary can hold a value that is another dictionary

For example, let's think about television shows for a second.
Each TV show has a collection of seasons and each season has a collection of episodes.

'''

tv_shows = {
    
    "the wire": {
        
        "season 1": {
            
            "episodes": ["monster", "scary alien"],
            
            "genre": "science fiction",
            
            "year": 1992
        },
        
        "season 2": {
            
            "episodes": ["go ways", "ykyk"],
            
            "genre": "horror",
            
            "year": 1995
            
        }
    },
    
    "the blacklist": {
        
        "season 1": {
            
            "episodes": ["gotei 13"],
            
            "genre": "crime",
            
            "year": 2000
            
        }
    }
}

# finding the second episode of the first season of the wire
print(tv_shows["the wire"]["season 1"]["episodes"][1])

# the year of release for season two of the wire
print(tv_shows["the wire"]["season 2"]["year"])

#  the genre for season one of the black list
print(tv_shows["the blacklist"]["season 1"]["genre"])