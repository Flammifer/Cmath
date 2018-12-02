from math import exp, cos, sin
def func(x):
    return x**2-2*x

def bin_search(F, a, b, eps = 10**(-8)):
    c = 0
    flag = 1
    while flag:
        c = (a+b)/2
        fa = F(a)
        fb = F(b)
        fc = F(c)
        if (fc*fa)>=0:
            if (fc*fb) <= 0:
                a = c
            else:
                return
        if (fc*fa) <= 0:
            if (fc*fb) >= 0:
                b = c
            else: return
        if abs(fc) < eps:
            return c

def check_extr(F, x, step = 10**(-5)):
    d2 = (F(x+step)-F(x-step))/(2*step)
    if (d2 > 0):
        return 1
    else: return 0
print(bin_search(func, -1, 1))
print(bin_search(func, 1, 3))
print(check_extr(func, 0.0))
print(check_extr(func, 2.0))
