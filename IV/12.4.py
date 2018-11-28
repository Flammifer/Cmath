from math import exp, cos, sin
def xex(x):
    return x**2-exp(x)/5

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

print(bin_search(xex, 3, 5))

def cossin(x):
    return cos(sin(x)-1.32) - x + 0.85
def sincos(y):
    return sin(cos(y)+0.85) - y - 1.32

print(bin_search(cossin, -10, +10))
print(bin_search(sincos, -10, +10))
