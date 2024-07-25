def pairs(a, x, y, z):
    n = sorted([a, x, y, z])
    if n[0] + n[3] == n[1] + n[2]:
        return 1
    return 0

def f(a, x, y, z):
    return pairs(a, x, y, z) or (pairs(x, z, 24, 13) == pairs(a, 5, 8, 19))

m = 0
ma = 0

for a in range(100):
    c = 0
    for x in range(1, 50):
        for y in range(1, 50):
            for z in range(1, 50):
                if f(a, x, y, z):
                    c += 1
    if c > m:
        m = c
        ma = a

print(ma)