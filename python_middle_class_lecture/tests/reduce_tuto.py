from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))  # 누적
