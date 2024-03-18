# Task1
squares = [x ** 2 for x in range(1, 11)]


# Task2
def generate_squares(start, end):
    return [x ** 2 for x in range(start, end + 1)]


# Task3
class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end + 1)]

