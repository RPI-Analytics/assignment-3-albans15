import numpy as np


def divby2(x):
    divby2=list(filter(lambda x: x % 2 == 0, x))
    return divby2
divby2

numbers = [3, 12, 91, 33, 21, 34, 54, 34, 34, 54]
print(divby2(numbers))
