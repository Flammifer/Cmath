from math import exp
import numpy as np
J = np.array([(998,  1998) ,(-999,-1999)])
h = [10**(-4), 10**(-3), 0.0025, 5*10**(-3), 0.01]
def solution(t):
    return (-3*(exp(-1000*t)) + 4*(exp(-t)), 3*(exp(-1000*t)) -2*(exp(-t)) )


def trapeze(h, ini_vec,  t_ini = 0.0, t_fin = 10.0):
    t = t_ini
    y_np = np.array([0,0]) #y_n+1 =  ...
    y_n = np.array([ini_vec[0], ini_vec[1]])
    A = np.array([[1,0], [0,1]]) - np.dot(J, h/2)

    for i in range(1, int((t_fin-t_ini)/h)+1):
        t = t_ini + i*h
        B = y_n + np.dot(np.dot(J, y_n), h/2)
        #print('t = ', t, ' A, B', A, B)
        y_np = np.linalg.solve(A, B)
        y_n = y_np[:]
        #print(y_np)
    print(t)
    return y_np
def check(vec, t):
    return (abs(vec[0]-solution(t)[0]) + abs(vec[1]-solution(t)[1]))/(abs(solution(t)[0]) + abs(solution(t)[1]))
def cros(h, ini_vec, t_ini = 0.0, t_fin = 10.0):
        t =  t_ini
        sol = np.array([ini_vec[0], ini_vec[1]])
        E = np.array([[1,0], [0,1]])
        for i in range(1, int((t_fin-t_ini)/h)+1):
            t = t_ini + i*h
            tmp =np.linalg.solve(np.add(E, -h*complex(1/2, 1/2 )*J) , np.dot(J,sol) )
            sol = np.add(sol, h*(tmp.real))
        return sol


#print("trapeze", check(trapeze(h[0], (1,1)), 10))
for i in range(5):
    print("trapeze, h = ", h[i], 'Accuracy = ',  check(trapeze(h[i], (1,1)), 10))
    print("CROS, h = ", h[i], 'Accuracy = ', check(cros(h[i], (1,1)),10))
