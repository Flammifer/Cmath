from math import exp
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
