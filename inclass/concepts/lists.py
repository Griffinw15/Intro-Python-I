# In Python, arrays are called lists 
​
# Create an empty list 
l = []
​
# create a list with some numbers 
n = [10, 60, 20, 5]
​
# add a number to n 
n.append(77)
​
# print our list n
print(n)
​
# print out each element in the n one at a time 
for elem in n:
    print(elem)
​
# what if we also want the index of the element? 
# enumerate gives us access to each list element and its index 
for index, elem in enumerate(n):
    print(f"Element {index} is {elem}")
​
# How do we just loop a certain number of times? 
# range(10) == range(0, 10, 1)
for x in range(10):
    print(x)