class SimpleCalculator:
    def __init__(self):
        self.first_input = None
        self.second_input = None

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

try:
    while True:
        calculator