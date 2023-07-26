'''
Now, a more Pythonic approach for this problem is the items method.

The items method is invoked on a dictionary object and returns and iterable view object.

It is an iterator object, which is a special object that yields one key value pair at a time for each

iteration, where each round it's actually going to provide us a two element tuple where the first element

is the key.

And the second element is that keys corresponding value the tuples elements, i.e. the dictionary key

and the value can then be unpacked and stored in two variables right in the declaration of the formal.

'''

'''
in java using iterator object

Map<Integer, Integer> map = new HashMap<Integer, Integer>();
Iterator<Map.Entry<Integer, Integer>> entries = map.entrySet().iterator();
while (entries.hasNext()) {
    Map.Entry<Integer, Integer> entry = entries.next();
    System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
}
'''

college_courses = {
    
    "itec 120": "mrs. brennaman",
    
    "linear algebra": "dr. paul duty",
    
    "philosophy": "aristotle"
    
}

# using iterator object and unpacking dic to a tuple 
for course, professor in college_courses.items():
    
    print(f"the course {course} is taught by {professor}")

# community convention when getting only one
for _, professor in college_courses.items():
    
    print(f"the next professor is {professor}")
    
    
    
    
