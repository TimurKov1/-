def sequence(a, x, y):
    n = sorted([a, x, y])
    if n[2] - n[1] == n[1] - n[0]:
        return 1
    return 0

def f(a, x, y):
    return ((not sequence(a, x, y)) <= sequence(a, 20, 18))

s = 0
for a in range(1, 100):
    if all(f(a, x, y) for x in range(1, 300) for y in range(1, 300)):
        s += a

print(s)