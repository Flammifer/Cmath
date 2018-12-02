import numpy as np

def bin_search(F, a, b,  *args):
    eps = 10**(-10)
    c = 0
    flag = 1
    while flag:
        c = (a+b)/2
        if len(args)> 0:
            fa = F(a, args)
            fb = F(b, args)
            fc = F(c, args)
        else:
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



def gradient(F, w, step = 0.1):
    grad = []
    for i in range(len(w)):
        u = []
        o = []
        for j in range(len(w)):
            if i == j:
                u.append(w[j]-step)
                o.append(w[j]+step)
            else:
                u.append(w[j])
                o.append(w[j])
        grad.append((F(o)- F(u))/(2*step))
    return grad #Градиент F в точке w

def vec_norm(x):
    t = 0
    for i in x:
        t += abs(i)
    return t
def vec_mul(x, vec): #умножение веткора на число
    res = []
    for i in vec:
        res.append(x*i)
    return res
def vec_prod(x, y):
    tmp = 0.0
    for i in range(len(x)):
        tmp += x[i]*y[i]
    return tmp
def vec_sum(x, y):
    s = []
    if (len(x) != len(y)):
        return s
    for i in range(len(x)):
        s.append(x[i]+y[i])
    return s
def vec_uni(x): #сделать вектор единичным
    s = 0
    for i in x:
        if (abs(i)>s): s = abs(i)
    y = []
    for i in x:
        y.append(np.divide(i, s))
    return y


'''
def f(x):
    return x

def func(funci, x, y,  *args):
    print(funci(args))
func(f, 1, 2, [1, 2])
'''
