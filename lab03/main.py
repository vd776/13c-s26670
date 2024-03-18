# Task1
squares = [x ** 2 for x in range(1, 11)]


# Task2
def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


# Task3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end + 1)]


# Task4
import math

square_generator = SquareGenerator()
squares = square_generator.generate_squares(1, 0)
square_roots = [math.sqrt(x) for x in squares]



# Task5

class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End must be greater than start")
        return [x**2 for x in range(start, end + 1)]
