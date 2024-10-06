class Shopping:
    def __init__(self,name):
        self.name = name 
        self.cart = []

    def add_to_cart(self,item,price,quantity):
        product = {'item':item, 'price':price, 'quantity':quantity}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('total price:', total)
        if amount < total:
            print( f"Please provide {total-amount} more")
        else:
            extra = amount-total
            print(f"Here is your items and extra amount {extra}")

    def remove_from_cart(self,item_name):
        for i in self.cart:
            if i['item'] == item_name:
                print(f"{i} successfully removed")
                self.cart.remove(i)
                print(self.cart)
                return
            else:
                print(f"{item_name} not found")
        

swapan = Shopping('Allen')
swapan.add_to_cart('Alu',50,6)
swapan.add_to_cart('Dim',100,10)

print(swapan.cart)
swapan.checkout(1500)
swapan.remove_from_cart('Dim')