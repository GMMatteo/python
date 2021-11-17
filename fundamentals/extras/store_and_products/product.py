class Product:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price = ((self.price * percent_change) + (self.price))
        else:
            self.price = ((self.price) - (self.price * percent_change))
            return self

    def print_info(self):
        print("Product Name: {}\n Price: {}\n Category: {}".format(self.name, self.price, self.category))
        return ("Product Name: {} Price: ${} Category: {}".format(self.name, self.price, self.category))

    def product_name(self):
        print("{}".format(self.name))
        return self.name
    
    def product_price(self):
        print("{}".format(self.price))
        return self.price

# def createProduct():
#         name = input("Product Name ")
#         price = input("Product Price ")
#         category = input("Product Category ")
#         return Product(name, price, category)

# a = Product('Oreo',5, 'Snacks')
# b = Product('Feta', 3.99, 'Cheese')
# c = Product('Guinness', 2.50, 'Beer')
# d = Product('Bacon', 3.75, 'Meat')
# a.update_price(.07, False)
# b.update_price(.03, True)
# c.update_price(.07, False)
# d.update_price(.04, True)
# a.product_name()
# a.print_info()
# print(a.name)
# b.product_name()
# b.print_info()
# print(b.name)
# c.product_name()
# c.print_info()
# print(c.name)
# d.product_name()
# d.print_info()
# print(d.name)
