import numpy as np
from math import sin, pi, exp

def shuttle(A, C, f): #прогонка для матриц с одинаковыми диагоналями. M = ((C, A, 0 ...), (A, C, A, 0, 0, ..)
    N = len(f)
    x = np.array([0.0]*N)
    Cn = np.array([0.0]*N)
    Cn[0] = C
    Fn = np.array([0.0]*N)
    Fn[0] = f[0]
    G = A*A
    for i in range(1, N):
        Cn[i] = C - np.divide(G, Cn[i-1])
        Fn[i] = np.add(f[0], -np.divide(np.multiply(A, Fn[i-1]), Cn[i-1]))
    x[N-1] = Fn[N-1]/Cn[N-1]

    for i in range(N-2, -1, -1):
        x[i] = (Fn[i] - A*x[i+1])/(Cn[i])
    return x
N = 1000 #количество узлов
h = 1/N
tau = h

def check(x, t, u):
    return ((1-exp(-t*pi**2))*sin(pi*x) - u)/(1-exp(-t*pi**2))*sin(pi*x)

E = np.identity(N-2)
Lxx = np.array([[0.0]*(N-2)]*(N-2))
for i in range(N-2):
    for j in range(N-2):
        if i==j: Lxx[i][j] = - 2
        else:
            if abs(i-j) == 1: Lxx[i][j] = 1 ## Lxx matrix

u = np.array([[0.0]*(N-2)]*(N))
#u[2][0] = 1000
#print(u)

f = [0.0]*(N-2)
for i in range(N-2):
    f[i] = tau*pi**2 * sin(pi*(i+1)/(N-1))


for i in range(1, N): #идем по строкам сетки вверх
    Q = np.dot((E+tau/2 * Lxx/h**2), u[i-1]) + f
    #u[i] = shuttle(-tau/(2*h**2), 1 + tau/(h**2), Q)
    u[i] = np.linalg.solve(((E-tau/2 * Lxx/h**2)), Q)
w = np.array([[0.0]*N]*N)
var = np.array([[0.0]*N]*N)
for i in range(N):
    for j in range(N):
        if j==0 or j==N-1:
            w[i][j] = 0.0
            var[i][j] = 0.0
        else:
            w[i][j] = u[i][j-1]
            if (abs(u[i][j-1]) > 0):
                var[i][j] = check(j*h, i*tau, u[i][j-1])
print(np.max(var))
