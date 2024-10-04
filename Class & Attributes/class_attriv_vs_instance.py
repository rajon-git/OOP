class Shop:
    # cart = [] #class attribute
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart= [] # instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)

mehjabeen = Shop('Meh Jabeen')
mehjabeen.add_to_cart('Shoe')
mehjabeen.add_to_cart('Phone')
print(mehjabeen.cart)

nisho = Shop('Nisho')
nisho.add_to_cart('Cap')
nisho.add_to_cart('Pant')
print(nisho.cart)