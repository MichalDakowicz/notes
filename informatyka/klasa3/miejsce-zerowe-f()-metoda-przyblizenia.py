def f(x):
    return 2 * x - 2

def miejsce_zerowe(a, b, epsilon):
    if f(a) * f(b) > 0:
        return None
    while True:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < epsilon:
            return c

print(miejsce_zerowe(0, 10, 0.0001))