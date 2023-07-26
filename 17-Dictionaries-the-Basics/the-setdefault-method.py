# used to write a key value pair to a dictionary if the key does not already exist.

film_directors = {
    
    "the godfather": "francis ford",
    
    "the rock": "michael bay",
    
    "goodfellas": "me"
    
}

print(film_directors.get("goodfellas"))
print(film_directors.get("bad boys", "michael bay"))
print()

film_directors.setdefault("bad boys")
print(film_directors)

print()
film_directors.setdefault("bad boys", "a good director")

print(film_directors)

mystery = {
    "A": 5,
    "a": 2,
    "B": [30, 40]
}