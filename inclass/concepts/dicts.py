# Analogous to JS's objects 
​
# create an empty dict 
d = {}
​
# create a dict with some key-value pairs 
e = {"foo": 12, "bar": 20}
​
k = {10: "baz", 15: "car", "foo": {1: 2, 3: 4, 5: 6, 0: 7} }
​
f = {1: 2, 3: 4, 5: 6, 0: 7} 
​
# the `keys` method populates a list with all of the keys of a dict 
print(f.keys())
​
print(k["foo"][1])
​
# how do we access a value in a dict? 
# access it via its key using bracket notation 
# there is no accessing of dict values via dot notation 
# print(e["foo"])
# print(k[15])
​
# iterate through a dictionary 
# without using a special method, when we iterate, we
# only get access to the keys 
# for key in k:
#     print(f"Key: {key}, value: {k[key]}")
​
# # we can access keys and values directly when iterating using 
# # the special method `items()`
# for key, value in k.items():
#     print(f"Key: {key}, value: {value}")