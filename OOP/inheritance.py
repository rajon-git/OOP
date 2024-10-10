#base class, parent class, common class

class Device:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        print(f"Running device: {self.brand}")

class Laptop:
    def __init__(self, memory):
        self.memory = memory

    def coding(self):
        print(f"Learning python")

class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def change_lens(self):
        print(f"Learning django")

class Phone(Device):
    def __init__(self, dual_sim,brand,price,color):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color)

    def phone_call(self):
        print(f"Opening Phone")
    
    def __repr__(self):
        return f"phone: {self.dual_sim}, {self.brand}, {self.price}, {self.color}"
    
my_phone = Phone('New','Iphone',120000,'Black')
print(my_phone)