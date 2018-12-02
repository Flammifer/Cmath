import MyMath as mm

def func(x):
    return x**2-2*x



def check_extr(F, x, step = 10**(-5)):
    d2 = (F(x+step)-F(x-step))/(2*step)
    if (d2 > 0):
        return 1
    else: return 0
print(mm.bin_search(func, -1, 1))
print(mm.bin_search(func, 1, 3))
print(check_extr(func, 0.0))
print(check_extr(func, 2.0))
