# should Department inherit from Store? 
class Department:
    def __init__(self, dept_id, name, products):
        self.dept_id = dept_id
        self.name = name
        self.products = products
​
    def __str__(self):
        return f"{self.dept_id}: {self.name}"
​
    def print_products(self):
        for i, p in enumerate(self.products):
            print(f"{i+1} - {p}")