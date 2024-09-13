def pierwiastek(P, epsilon):
    a = 1
    a_prim = P
    while abs(a - a_prim) > epsilon:
        a = (a + a_prim) / 2
        a_prim = P / a
    return a

print(pierwiastek(4, 0.001))