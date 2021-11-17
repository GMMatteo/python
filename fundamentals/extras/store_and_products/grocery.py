from product import Product
from store import Store

a = Product('Oreo',5, 'Snacks')
b = Product('Feta', 3.99, 'Cheese')
c = Product('Guinness', 2.50, 'Beer')
d = Product('Bacon', 3.75, 'Meat')

s = Store("Store Name Is Lucky")

print(s.name)
s.add_product(a.print_info()).add_product(b.print_info()).add_product(c.print_info()).add_product(d.print_info())
s.add_product(a.product_name()).add_product(b.product_name()).add_product(c.product_name()).add_product(d.product_name())
s.sell_product(0).sell_product(2)