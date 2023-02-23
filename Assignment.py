import math

# This class represents Complex numbers, where the real and imaginary parts are represented by real numbers.
# The class ComplexNumber also defines and implements some basic functionalities for complex numbers arithmetics.
# The arithmetic functionalities implemented include addition, substraction, multiplication and division between two 
# complex numbers, leaving such operations with other number types not implemented.
# This class also includes functionalities for absolute value and a string representation of complex numbers, as well as 
# equality between two different complex numbers.
class ComplexNumber :

    # Constructor
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.img + other.img)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.img - other.img)
        else:
            return NotImplemented
    
    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.img * other.img
            img = self.real * other.img + self.img * other.real
            return ComplexNumber(real, img)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, ComplexNumber):
            denominator = other.real ** 2 + other.img ** 2
            real = (self.real * other.real + self.img * other.img) / denominator
            img = (self.img * other.real - self.real * other.img) / denominator
            return ComplexNumber(real, img)
        else:
            return NotImplemented
    
    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.img ** 2)

    def __str__(self):
        sign = "+" if self.img >= 0 else "-"
        return f"{self.real}{sign}{abs(self.img)}i"

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

    # TODO: other functionalities that can be implemented include (but are not limited to) conjugation, square root, power of a complex number
    # and reciprocal of a given complex numbers. All functions can also be including operations between complex numbers and
    # other base types available in Python, such as floats or integers.

    def test_complex_numbers():
        # Test addition
        assert ComplexNumber(1,2) + ComplexNumber(3,4) == ComplexNumber(4,6)
        assert ComplexNumber(1,2) + 3 == NotImplemented
        
        # Test substraction
        assert ComplexNumber(1,2) - ComplexNumber(3,4) == ComplexNumber(-2,-2)
        assert ComplexNumber(3,4) - ComplexNumber(1,2) == ComplexNumber(2,2)
        assert ComplexNumber(1,2) - 3 == NotImplemented

        # Test multiplication
        assert ComplexNumber(1,2) * ComplexNumber(3,4) == ComplexNumber(-5,10)
        assert ComplexNumber(1,2) * 3 == ComplexNumber(3,6)

        # Test division
        assert ComplexNumber(1,2) / ComplexNumber(3,4) == ComplexNumber(0.44, 0.8)
        assert ComplexNumber(1,2) / 0 == NotImplemented

        # Test absolute value
        assert abs(ComplexNumber(1,2)) == 2.24

        # Test equality
        assert ComplexNumber(1,2) == ComplexNumber(1,2)