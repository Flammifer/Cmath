import MyMath as mm

def func(x):
    return x**3/3+x**2

def dihotom(F, a, b, eps = 10**(-8)):
    while 1:
        d = (b-a)/50
        c = (b+a)/2
        u1, u2 = c-d, c+d

        if (F(u1)<F(u2)):
            b = u2
        else: a = u1

        if (b-a)<eps:
            return (b+a)/2






def check_extr(F, x, step = 10**(-5)):
    d2 = (F(x+step)-F(x-step))/(2*step)
    if (abs(d2) < 10**(-5)):
        return 1
    else: return 0
print(dihotom(func, -1, 1))
print(dihotom(func, -3, -1))

print(check_extr(func, 0.0))
print(check_extr(func, -5.0))
