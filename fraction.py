class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def reduce(self):
        if self.numerator == 0:
            self.denominator = 1
        elif self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator
        common_divisor = self.gcd(abs(self.numerator), self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + '/' + str(self.denominator)


frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)
result = frac1 + frac2
print(result)
print(str(frac1), str(frac2))
