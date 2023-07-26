# you can or remove a key value pair in dictionary
# if the key does not exist and the user tries to access it, python will automatically add a key-value pair

roster = {
    
    "man utd": ["sancho", "amad", "licha"],
    
    "arsenal": ["saka", "odegard", "havertz"]
    
}

# print(roster["liverpool"]) raises a value error

# adding a key value pair after the dictionary is already made
roster["liverpool"] = ["macallister", "salah", "thiago"]

# print(roster["liverpool"])

print(roster.pop("arsenal"))

roster["arsenal"] = ["saka"]

print(roster)

print()

# both are the same 
video_games = {} # this is preffered
# video_games = dict()

video_games["subtitles"] = True
video_games["difficulty"] = "recruit"
video_games["volume"] = 7

print(video_games)

video_games["difficulty"] = "hard" # changing difficulty
video_games["subtitles"] = False # changing subtitles

# key can be dynamic
words = ["danger", "beware", "danger", "beware"]

def count_words(words):
    
    empty_hashmap = {}
    
    for i in words:
        
        if i in empty_hashmap: # dynamically accessing a key
            
            empty_hashmap[i] += 1 # if it already exist still add it
            
        else:
            
            empty_hashmap[i] = 1 # none repeated words
            
    return empty_hashmap

print(count_words(words))
            
            




