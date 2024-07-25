def simple(x, y):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0 and y % i == 0:
            return 0
        if x % (x // i) == 0 and y % (x // i) == 0:
            return 0
    return 1

def f(x, a):
    return simple(x, a) or (simple(a, 29) <= simple(x, 19))

for a in range(2, 100):
    if all(f(x, a) for x in range(1, 1000)):
           print(a)
           break