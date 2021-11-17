from product import Product

# a = Product('Oreo',5, 'Snacks')
# b = Product('Feta', 3.99, 'Cheese')
# c = Product('Guinness', 2.50, 'Beer')
# d = Product('Bacon', 3.75, 'Meat')


class Store:

    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, new_product):
        # self.new_product = new_product
        # new_product = Product.name
        Store.products.append(new_product)
        return self

    def sell_product(self, id):
        print("Sold ", Store.products.pop(id))
        return self
        # self.id = id

    def inflation(self, percent_increase):
        # priceList = [a.price, b.price, c.price, d.price]
        # for index, item in enumerate(priceList):
	    #     priceList[index] = ((priceList[index] * percent_increase) + (priceList[index]))
        # a.price = priceList [0]
        # b.price = priceList [1]
        # c.price = priceList [2]
        # d.price = priceList [3]
        # return self
        pass

    def set_clearance(self, percent_discount):
        # category = [a.category, b.category, c.category, d.category]
        # priceList = [a.price, b.price, c.price, d.price]
        # # print(category)
        # for items in category:
        #     # print(items)
        #     if items == 'Meat' or items == 'Cheese' :
        #         for index, item in enumerate(priceList):
        #             priceList[index] = ((priceList[index]) - (priceList[index] * percent_discount))
        #         a.price = a.price
        #         b.price = priceList [1]
        #         c.price = c.price
        #         d.price = priceList [3]
        #         print(a.print_info())
        #         print(b.print_info())
        #         print(c.print_info())
        #         print(d.print_info())
        #         return self
        pass

# def createStore():
#         name = input("Store Name ")
#         return Store(name)

s = Store("Store Name Is Lucky")
# # s.set_clearance(.04)
# s.inflation(.04)
# s.set_clearance(.07)
# # s.add_product(a.print_info()).add_product(b.print_info())
# # s.add_product(a.print_info()).add_product(b.print_info()).add_product(c.print_info()).add_product(d.print_info())
# # s.add_product(a.product_name()).add_product(b.product_name()).add_product(c.product_name()).add_product(d.product_name())
# # s.sell_product(0).sell_product(2)
# # print(s.products)
# # print(s.name)

# s.add_product(a.print_info()).add_product(b.print_info()).add_product(c.print_info()).add_product(d.print_info())
# print(s.products)
# s.inflation(.04)
# print(s.products)
# s.set_clearance(.07)
# print(s.products)
# s.sell_product(0).sell_product(2)
# print(s.products)