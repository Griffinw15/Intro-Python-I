# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

#similar to y = [i for i in x if int(i) % 2 == 0]

def is_even(num):
    if int(num) % 2 == 0:
        return True

print(is_even(2))

# Read a number from the keyboard
num = input("Enter a number: ")
#num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def even_odd(num):
    if int(num) % 2 == 0:
        return "Even!"
    else:
        return "Odd"

print(even_odd(num))