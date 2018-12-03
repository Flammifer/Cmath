import MyMath as mm

def func(x):
    return x**3/3+x**2

def dihotom(F, a, b, eps = 10**(-8)):
    a0 = a
    b0 = b
    c = (a+b)/2
    k = 0
    while 1:
        yk = (a0+c)/2
        if (F(yk) <= F(c)): # step 1 a)
            b0 = c
            c = yk
        else: # setp 2 b)
            zk = (c+b0)/2
            if (F(c)<= F(zk)):
                a0 = yk
                b0 = zk
            else:
                a0 = c
                c = zk
        k += 1
        if (b0-a0) < 10**(-5):
            print("Steps: ", k)
            return (b0+a0)/2

def check_extr(F, x, step = 10**(-5)):
    d2 = (F(x+step)-F(x-step))/(2*step)
    if (abs(d2) < 10**(-5)):
        return 1
    else: return 0

print(dihotom(func, -1, 1))
print(dihotom(func, -33, -1))

print(check_extr(func, 0.0))
print(check_extr(func, -5.0))

