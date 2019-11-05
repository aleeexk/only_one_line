import math
from functools import reduce
from decimal import Decimal

lst = [1, 8, 7, 9, 2, 5, 7, 7, 9, 3, 4]

print(reduce((lambda x, y: x * y), [i + 1 for i in range(1000)]))
print(sum(range(1, 2 ** 25)))
print([j + str(i) for i in range(1, 11) for j in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']])
print([i * 2 if i % 2 else i for i in lst])
print(str(4 + Decimal(reduce((lambda x, y: x + y), [(4 / (2 * i + 3)) * ((-1) ** (i + 1)) for i in range(10 ** 6)])))[:22])
