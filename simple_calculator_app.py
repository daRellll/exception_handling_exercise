class SimpleCalculator:
    def __init__(self, first_input, second_input):
        self.first_input = first_input
        self.second_input = second_input

    def get_input(self):
        self.first_input = int(input("Enter your first number: "))
        self.second_input = int(input("Enter your second number: "))


