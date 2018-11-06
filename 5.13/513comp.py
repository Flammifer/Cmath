import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
def linear_f(x, a, b):
    return a*x+b;
x = [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
y = [431,409,429,422,530,505,459,499,526,563,587,595,647,669,746,760,778,828,846,836,916,956,1014,1076,1134,1024]
#first part is done via simple way (normal man)
#Now let's try to do it by myself
def f1(x):
    if (x>=20) and (x<= 28):
        return (-1/8*x + 3.5)
    else: return 0
def f2(x):
    if (x>=20) and (x<= 28):
        return (+1/8*x - 2.5)
    elif ( x>28) and (x<= 39):
        return (-1/11*x + 39/11)
    else: return 0
def f3(x):
    if (x>=28) and (x<= 39):
        return (+1/11*x - 28/11)
    elif ( x>39) and (x<= 45):
        return (-1/6*x + 7.5)
    else: return 0
def f4(x):
    if (x>=39) and (x<= 45):
        return (1/6*x - 6.5)
    else: return 0
def linear_combination(t, w):
    result = []
    for x in t:
        result.append( w[0]*f1(x)+w[1]*f2(x)+w[2]*f3(x)+w[3]*f4(x))
    return result
def F(x, y, w): #functional
    t = 0
    for i in range(len(x)):
        t += (w[0]*f1(x[i])+w[1]*f2(x[i])+w[2]*f3(x[i])+w[3]*f4(x[i]) - y[i])**2
    return t
flag = 1
step = 1
n = 0
lambda_ = 0.01
epsilon = 0.0001
w = [0, 0, 0, 0]
while flag:
    n += 1
    grad = []
    #lambda_ = lambda_*0.95
    for i in range(len(w)):
        flag2 = 1
        k = 1 #bool
        while flag2:
            u = []
            o = []
            for j in range(len(w)):
                if i == j:
                    u.append(w[j]-step)
                    o.append(w[j]+step)
                else:
                    u.append(w[j])
                    o.append(w[j])
            derivative = ((F(x, y, o)- F(x, y, u))/(2*step))
            if (k):
                grad.append(derivative)
            k = 0
            w[i] -= lambda_*derivative
            if (abs(derivative) < epsilon):
                flag2 = 0
        tmp = 0
        for k in grad:
                tmp += abs(k)
        if (tmp< 2*len(w)*epsilon):
            flag = 0
print(w, grad)
print(n)
t = np.linspace(20, 45, 100)
fig = plt.figure()
ax1 = fig.subplots()
popt_n, pcov_n, = curve_fit(linear_f, x, y)
ax1.plot(t, np.polyval(popt_n, t), 'g' )
ax1.plot(t, linear_combination(t, w), 'r' )
ax1.errorbar(x, y, fmt = '.')
plt.grid(True)
plt.show()
