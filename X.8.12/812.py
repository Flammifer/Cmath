from math import exp
import numpy as np
J = np.array([(998,  1998) ,(-999,-1999)])
h = [10**(-4), 10**(-3), 0.0025, 5*10**(-3), 0.01]
def solution(t):
    return (-3*(exp(-1000*t)) + 4*(exp(-t)), 3*(exp(-1000*t)) -2*(exp(-t)) )
def Adams(h, ini_vec,  t_ini = 0.0, t_fin = 10.0):
    t = t_ini
    sol_ = [ini_vec[0], ini_vec[1]] #я не буду ничего хранить, кроме предыдущего. т.к. k==1
    sol = sol_[:]
    while t < t_fin:
        t  += h
        sol[0] += np.multiply(np.sum([J[0][0]*sol_[0] , J[0][1]*sol_[1]]), h)
        sol[1] += np.multiply(np.sum([J[1][0]*sol_[0] , J[1][1]*sol_[1]]), h)
        sol_ = sol[:]
    return sol
def check(vec, t):
    return (abs(vec[0]-solution(t)[0]) + abs(vec[1]-solution(t)[1]))/(abs(solution(t)[0]) + abs(solution(t)[1]))


def CROS(h, ini_vec, t_ini = 0.0, t_fin = 10.0):
        t = t_ini
        sol = np.array([ini_vec[0], ini_vec[1]])
        E = np.array([[1,0], [0,1]])
        while t < t_fin:
            t  += h
            tmp =np.linalg.solve(np.add(E, -h*complex(1/2, 1/2 )*J) , np.dot(J,sol) )
            sol = np.add(sol, h*(tmp.real))
        return sol



for i in range(5):
    print("Adams", check(Adams(h[i], (1,1)), 10))
    print("CROS", check(CROS(h[i], (1,1)),10))
