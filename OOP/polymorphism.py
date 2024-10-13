class Animal:
    def __init__(self, name) -> None:
        self.name= name

    def make_sound(self):
        print("Animal making sound some")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Meau Meau")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Gheu Gheu")

don = Cat('Real Don')
don.make_sound()

shepard = Dog('shepard')
shepard.make_sound()