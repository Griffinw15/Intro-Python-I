# let's say we want to turn this list of tuples containing 
# the names and ages of people and turn it into a dictionary
names_and_ages = [
    ("Sarah", 22), 
    ("jorge", 50), 
    ("sam", 38),
    ("frank", 27),
    ("bob", 39),
    ("sandy", 46),
    ("shawn", 16),
]
​
d = {}
# with a for loop
# taking advantage of Python's automatic destructuring of tuples 
for name, age in names_and_ages:
    # assign the name as a key to our dict with the age as value 
    d[name] = age
​
# we want `name` as the key and `age` as the value
d = {name: age for name, age in names_and_ages}
​
