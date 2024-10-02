def call():
    print('Calling someone')
    return 'call done'

class Phone:
    price = 1200
    color = 'Blue'
    brand = 'Samsung'
    features = ['camera', 'spekar', 'hammer']

    def call(self):
        print('Calling one person')

    def send_sms(self,number, sms):
        result = f"Sending sms to: {number} and text is {sms}"
        return result

my_phone  = Phone()
print(my_phone.features)
my_phone.call()
print(my_phone.send_sms('01990020467','Hello brother how are you!'))