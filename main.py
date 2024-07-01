class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def set_fraction(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def display_fraction(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator + other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def subtract(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator - other_fraction.numerator * self.denominator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def multiply(self, other_fraction):
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def divide(self, other_fraction):
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fraction(new_numerator, new_denominator)

# Пример использования класса для арифметических операций:
fraction1 = Fraction(2, 4)
fraction2 = Fraction(2, 9)

add_result = fraction1.add(fraction2)
sub_result = fraction1.subtract(fraction2)
mul_result = fraction1.multiply(fraction2)
div_result = fraction1.divide(fraction2)

print(f"Результат сложения : {add_result.display_fraction()}")
print(f"Результат вычитания : {sub_result.display_fraction()}")
print(f"Результат умножения : {mul_result.display_fraction()}")
print(f"Результат деления : {div_result.display_fraction()}")
