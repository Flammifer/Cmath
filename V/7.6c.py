import matplotlib.pyplot as plt
import numpy as np
import MyMath as mm

def F(x):
    return x[0]**2+x[1]**2+x[0]*x[1]+x[0]-x[1]+1

def min_lambda(lambda_, args): #функция для нахождения оптимального лямбда
    w = args[0]
    fastest_grad = mm.vec_mul(-1, args[1])
    return mm.vec_prod(fastest_grad, mm.gradient(F, mm.vec_sum(w, mm.vec_mul(lambda_, fastest_grad))))

eps = 10**(-5)
def fast_grad(func):
    flag1 = 1
    w = [1, 1]
    while flag1:
        fastest_grad = mm.gradient(F, w) #первоначальное направление
        lambda_ = mm.bin_search(min_lambda, 0, 2, w, fastest_grad)
        if (mm.vec_norm(fastest_grad) < eps):
            return w
        w = mm.vec_sum(w, mm.vec_mul((-1)*lambda_ , fastest_grad))
        
print(fast_grad(F))
