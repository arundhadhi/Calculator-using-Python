import math

class Calculator:
    def __init__(self):
        self.num_1 = None
        self.num_2 = None
        self.special_num = None

    def basic_calculation(self):
        while True:
            try:
                self.num_1 = float(input("Enter the first number: "))
                self.num_2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input :(")


    def scientific_calculation(self):
        while True:
            try:
                self.special_num = float(input("Enter a number for scientific calculation: "))
                break
            except ValueError:
                print("Invalid input :(")


    def add(self):
        print("Addition:",self.num_1 + self.num_2)

    def sub(self):
        print("Subtraction:",self.num_1 - self.num_2)

    def mul(self):
        print("Multiplication:",self.num_1 * self.num_2)

    def div(self):
        if self.num_2 == 0:
            print("Not defined")
        else:
            print("Division:",self.num_1 / self.num_2)

    def rem(self):
        if self.num_2 == 0:
            print("Not defined")
        else:
            print("Remainder:",self.num_1 % self.num_2)

    def power(self):
        print("Power calculation",self.num_1 ** self.num_2)

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
            print("Logarithm is only valid for positive numbers")

    def natural_log(self):
        if self.special_num > 0:
            print("Natural logarithm of the number:", math.log(self.special_num))
        else:
            print("Natural logarithm is only valid for positive numbers")

    def exp(self):
        print("Exponential of the number:", math.exp(self.special_num))

    def pi_value(self):
        print("Value of pi:",math.pi*(self.special_num))

    def square_root(self):
        if self.special_num >= 0:
            print("Square root of the number:", math.sqrt(self.special_num))
        else:
            print("Square root is not defined for negative numbers.")

    def rad(self):
        print("The number in radians:", math.radians(self.special_num))

calculation = Calculator()
operator = input("Enter the operation (+, -, *, /, %, **, sin, cos, tan, cosec, log, ln, exp, pi, sqrt, rad): ")

if operator in ["+", "-", "*", "/", "%", "**"]:
    calculation.basic_calculation()
    if operator == "+":
        calculation.add()
    elif operator == "-":
        calculation.sub()
    elif operator == "*":
        calculation.mul()
    elif operator == "/":
        calculation.div()
    elif operator == "%":
        calculation.rem()
    elif operator == "**":
        calculation.power()
elif operator in ["sin", "cos", "tan", "cosec", "log", "ln", "exp", "pi", "sqrt", "rad"]:
    calculation.scientific_calculation()
    if operator == "sin":
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
    elif operator == "exp":
        calculation.exp()
    elif operator == "pi":
        calculation.pi_value()
    elif operator == "sqrt":
        calculation.square_root()
    elif operator == "rad":
        calculation.rad()
else:
    print("Invalid operation")
