from functools import reduce
x = ["abcdef1234567890!@%#", "qww223"]

y = map(lambda a: filter(lambda b: b >= "1" and b <= "9", a), x)
sum = reduce(lambda x, acc: x + acc, [1,2,3,4,5,6,7,8,9])
print(sum)