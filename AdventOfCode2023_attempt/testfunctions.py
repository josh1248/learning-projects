from functools import reduce
print(reduce(lambda running_sum, x: running_sum + x, range(0, 11), 0))