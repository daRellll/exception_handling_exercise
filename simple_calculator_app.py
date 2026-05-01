class SimpleCalculator:
    def __init__(self):
        self.first_input = None
        self.second_input = None
        self.operation = None

    def get_input(self):
        self.first_input = int(input("Enter your first number: "))
        self.second_input = int(input("Enter your second number: "))

    def addition(self):
        return self.first_input + self.second_input

    def subtraction(self):
        return self.first_input - self.second_input

    def multiplication(self):
        return self.first_input * self.second_input

    def division(self):
        return self.first_input / self.second_input

    def choose_operation_handler(self):
        print('''Choose a math operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division''')
        self.operation = input("Selected operation: ")

        if self.operation == '1':



while True:
    try:
        calculator = SimpleCalculator()



    except ValueError, ZeroDivisionError:
