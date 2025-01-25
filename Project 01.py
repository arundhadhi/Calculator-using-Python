import math

class Calculator:
    def __init__(self):
        self.numbers = []
        self.special_num = None

    def input_numbers(self):
        while True:
            try:
                n = int(input("How many numbers do you want to calculate?: "))
                if n < 1:
                    print("Please enter a positive integer.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        self.numbers = []
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Enter number {i + 1}: "))
                    self.numbers.append(num)
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def scientific_calculation(self):
        while True:
            try:
                self.special_num = float(input("Enter a number for scientific calculation: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def add(self):
        print("Addition:", sum(self.numbers))

    def subtract(self):
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        print("Subtraction:", result)

    def multiply(self):
        result = 1
        for num in self.numbers:
            result *= num
        print("Multiplication:", result)

    def divide(self):
        if len(self.numbers) == 2:
            if self.numbers[1] == 0:
                print("Not defined.")
            else:
                print(f"Division: {self.numbers[0] / self.numbers[1]}")
        else:
            print("Division calculate exactly 2 numbers.")

    def modulus(self):
        if len(self.numbers) == 2:
            print(f"Modulus: {self.numbers[0] % self.numbers[1]}")
        else:
            print("Modulus operation calculate exactly 2 numbers.")

    def power(self):
        if len(self.numbers) == 2:
            print(f"Power calculation: {self.numbers[0] ** self.numbers[1]}")
        else:
            print("Power operation calculate exactly 2 numbers.")

    def sine(self):
        print("Sine of the number:", math.sin(math.radians(self.special_num)))

    def cosine(self):
        print("Cosine of the number:", math.cos(math.radians(self.special_num)))

    def tangent(self):
        print("Tangent of the number:", math.tan(math.radians(self.special_num)))

    def cosecant(self):
        if self.special_num == 0:
            print("Cosecant is undefined for 0 degrees.")
        else:
            print("Cosecant of the number:", 1 / math.sin(math.radians(self.special_num)))

    def logarithm(self):
        if self.special_num > 0:
            print("Logarithm (base 10) of the number:", math.log10(self.special_num))
        else:
            print("Logarithm is only valid for positive numbers.")

    def natural_log(self):
        if self.special_num > 0:
            print("Natural logarithm of the number:", math.log(self.special_num))
        else:
            print("Natural logarithm is only valid for positive numbers.")

    def square_root(self):
        if self.special_num >= 0:
            print("Square root of the number:", math.sqrt(self.special_num))
        else:
            print("Square root is not defined for negative numbers.")

    def exponential(self):
        print("Exponential (e^x) of the number:", math.exp(self.special_num))

    def pi_value(self):
        print("Value of pi multiplied by the number:", math.pi * self.special_num)

    def radians(self):
        print("Convert degrees to radians:", math.radians(self.special_num))


calculation = Calculator()


operator = input("Enter the operation (+, -, *, /, %, **, sin, cos, tan, cosec, log, ln, exp, pi, sqrt, rad): ")


if operator in ["+", "-", "*", "/", "%", "**"]:
    calculation.input_numbers()
    if operator == "+":
        calculation.add()
    elif operator == "-":
        calculation.subtract()
    elif operator == "*":
        calculation.multiply()
    elif operator == "/":
        calculation.divide()
    elif operator == "%":
        calculation.modulus()
    elif operator == "**":
        calculation.power()


elif operator in ["pi", "sin", "cos", "tan", "cosec", "log", "ln", "sqrt", "exp", "rad"]:
    calculation.scientific_calculation()
    if operator == "pi":
        calculation.pi_value()
    elif operator == "sin":
        calculation.sine()
    elif operator == "cos":
        calculation.cosine()
    elif operator == "tan":
        calculation.tangent()
    elif operator == "cosec":
        calculation.cosecant()
    elif operator == "log":
        calculation.logarithm()
    elif operator == "ln":
        calculation.natural_log()
    elif operator == "sqrt":
        calculation.square_root()
    elif operator == "exp":
        calculation.exponential()
    elif operator == "rad":
        calculation.radians()


else:
    print("Invalid operation.")
