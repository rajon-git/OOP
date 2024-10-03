class Phone:
    manufactured = 'China'

    def __init__(self,owner,brand,price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        print(f'Sending to: {phone} and say: {sms}')

my_phone = Phone('Rajon','Symphony',10000)
print(my_phone.owner, my_phone.brand, my_phone.price)

my_phone.send_sms(1990020467, 'Hi Nusayba')
her_phone = Phone('Nusayba','Symphony',100000)
print(her_phone.owner, her_phone.brand, her_phone.price)

her_phone.send_sms(1310561120, 'Hi Rajon')
