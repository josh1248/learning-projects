def fibs_up_to(cap):
    a, b = 0, 1
    while a <= cap:
        yield a
        a, b = b, a + b

for i in fibs_up_to(1000):
    print(i)