class User:
    def __init__(self, cart, money):
        #self.cart = cart
        self.cart = []
        self.money = money 
​
    def __str__(self):
        return f"Money: ${self.money}, Cart: {self.cart}"
​
    def print_status(self):
        print(f"Money: ${self.money}")
        print("Cart: ")
        for p in self.cart:
            p.print_name()
​
    def add_to_cart(self, product):
        # check to make sure User has enough money
        if self.money >= product.price:
            # subtract price of product from money
            self.money -= product.price
            # otherwise, add the product to their cart 
            self.cart.append(product) 
        else:
            print("You don't have enough money to buy that!\n")