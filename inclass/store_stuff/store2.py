import sys
​
from department import Department
from product import Product
from user import User
​
class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments
​
    def print_welcome(self):
        print(f"Welcome to {self.name}! Which department would you like to visit?")
​
        for d in self.departments:
            print(d)
​
store = Store("The Dugout", [
    Department(1, "Baseball", [
        Product("Kid's Bat", 20),
        Product("Bat", 70),
        Product("Catcher's Mitt", 30),
    ]),
    Department(2, "Basketball", [
        Product("Basketball", 15),
        Product("Shorts", 30),
        Product("Jersey", 45),
    ]),
    Department(3, "Football", [
        Product("Helmet", 150),
        Product("Cleats", 90),
    ]),
    Department(4, "Golf", [
        Product("Driver", 250),
        Product("Putter", 200),
        Product("Golf Balls", 30),
    ]),
])
​
# initialize a User 
# use command line arguments to initialize a User 
num_args = len(sys.argv)
​
if num_args < 2:
    money = 100
elif num_args == 2:
    money = sys.argv[1]
else:
    print("usage: store.py [money]")
    sys.exit(1)
​
# init the User 
user = User(money)
​
# loop forever while the user is browsing through departments 
# use the `input` function to prompt the user to select a department to browse 
while True:
    # print out the user's status 
    user.print_status()
    print()
​
    # print a welcome message for the Store
    store.print_welcome()
​
    # get the department number the user wants to visit:
    selection = input("Which department would you like to visit? ")
​
    # if the user types "quit", exit the program 
    if selection == "quit":
        break
​
    chosen_department = store.departments[int(selection)-1]
​
    print(f"You picked the {chosen_department.name} department.\n")
    print("Here are you the products available in this department: \n")
    products = chosen_department.products
    chosen_department.print_products()
    print()
​
    product_selection = input("Select a product to buy: ")
​
    # add the chosen product to the user's cart 
    chosen_product = products[int(product_selection)-1]
    user.add_to_cart(chosen_product)
​
# Define a User class 
# Add the ability to select products and add them to the user's cart
# Check the User's total amount of money before adding a product to their cart 
# Subtract the price of the product from their money total