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
Nx = 100 #количество узлов сетки по координате
Nt = 1000 #по времени
h = 1/(Nx-1)
tau = 1/(Nt-1)

def check(x, t, u):
    return ((1-exp(-t*pi**2))*sin(pi*x) - u)

E = np.identity(Nx-2)
Lxx = np.array([[0.0]*(Nx-2)]*(Nx-2))
for i in range(Nx-2):
    for j in range(Nx-2):
        if i==j: Lxx[i][j] = - 2
        else:
            if abs(i-j) == 1: Lxx[i][j] = 1 ## Lxx matrix

u = np.array([[0.0]*(Nx-2)]*(Nt))

f = [0.0]*(Nx-2)
for j in range(Nx-2):
    f[j] =tau* pi**2 * sin(pi*(j+1)/(Nx-1))


for i in range(1, Nt): #идем по строкам сетки вверх

    Q = np.dot(E + 0.5 * tau*Lxx/h**2, u[i-1])  + f
    u[i] = np.linalg.solve(((E-tau/2 * Lxx/h**2)), Q)
w = np.array([[0.0]*Nx]*Nt)
var = np.array([[0.0]*Nx]*Nt)
real = np.array([[0.0]*Nx]*Nt)
for i in range(Nt):
    for j in range(Nx):

        if j==0 or j==Nx-1:
            w[i][j] = 0.0
            var[i][j] = 0.0
            real[i][j] = 0.0
        else:
            w[i][j] = u[i][j-1]
            real[i][j] = check((j)*h, i*tau, 0)
            var[i][j] = abs(check(j*h, i*tau, u[i][j-1]))
print(np.max(var))
#print(w)
#print(var)
