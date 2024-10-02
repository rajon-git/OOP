class Calculator:
    brand = 'Casio MS990'

    def add(self, num1,num2):
        return f"Sum of {num1} and {num2} is: {num1+num2}"
    
    def sub(self, num1,num2):
        return f"Subtraction of {num1} and {num2} is: {num1-num2}"
    
    def mul(self, num1,num2):
        return f"Multiple of {num1} and {num2} is: {num1*num2}"
    
    def div(self, num1,num2):
        return f"Division of {num1} and {num2} is: {num1/num2}"
    
my_calculator = Calculator()
print(my_calculator.add(8,5))
print(my_calculator.sub(8,5))
print(my_calculator.mul(8,5))
print(my_calculator.div(8,5))