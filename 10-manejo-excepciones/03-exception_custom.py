class NegativeValueError(Exception):
    def __init__(self, value):
        super().__init__(f"Negative values are not allowed: {value}")

def calculate_square_root(number):
    if number < 0:
        raise NegativeValueError(number)
    return number ** 0.5

try:
    result = calculate_square_root(-25)
    print(f"The square root is: {result}")
except NegativeValueError as e:
    print(e)
# Output: Negative values are not allowed: -25