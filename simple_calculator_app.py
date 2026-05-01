class SimpleCalculator:
    def __init__(self):
        self.first_input = None
        self.second_input = None
        self.operation = None
        self.repeat = True

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
            print(f"sum = {self.addition()}")
        elif self.operation == '2':
            print(f"sub = {self.subtraction()}")
        elif self.operation == '3':
            print(f"mult = {self.multiplication()}")
        elif self.operation == '4':
            print(f"div = {self.division()}")
        else:
            print("Invalid operation")

    def try_again(self):
        self.user_response = input("Would you like to try again? (y/n): ")

        if self.user_response.lower() == 'y':
            pass
        else:
            print("Goodbye!")

calculator = SimpleCalculator()
while True:
    try:
        calculator.get_input()
        calculator.choose_operation_handler()

    except (ValueError, ZeroDivisionError):
        print("Invalid operation or input!")

