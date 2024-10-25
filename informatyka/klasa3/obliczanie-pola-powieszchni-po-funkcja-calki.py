def f(x):
    return x*x+1

def calka(a, b, epsilon):
    x = (b-a)/epsilon
    pole = 0
    for i in range(epsilon):
        y = f(a+i*x)
        pole += y*x
    return pole

print(calka(0, 4, 1000))

def calka_trapez(a, b, epsilon):
    x = (b-a)/epsilon
    pole = 0
    for i in range(epsilon):
        y1 = f(a+i*x)
        y2 = f(a+(i+1)*x)
        pole += (y1+y2)*x/2
    return pole

print(calka_trapez(0, 4, 100))