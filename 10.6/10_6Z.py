import numpy as np

#matrix input

num = 0

flag = False

a=10

dimension = 200

A = []
for i in range(dimension):
    A.append([])
    for j in range(i):
        A[i].append(np.divide(1,i+1))
    A[i].append(a)
    if(i != dimension - 1):
        A[i].append(np.divide(1,i+1))
    for j in range(i+2, dimension):
        A[i].append(0)
    A[i].append(i+1)
A = np.array(A)


def zeidelstep(approx):
    for i in range(dimension):
        tmp1 = 0
        tmp2 = 0
        for j in range(0,i):
            tmp1 = np.add(tmp1, np.multiply(A[i][j],approx[j]))
        for j in range(i+1,dimension):
            tmp2 = np.add(tmp2, np.multiply(A[i][j],approx[j]))
        approx[i] = np.divide(A[i][dimension]-tmp1-tmp2, A[i][i])

approx = np.zeros(dimension)
while not flag:
    num = num + 1
    old = np.copy(approx)
    zeidelstep(approx)
    tmp = 0
    for i in range(dimension):
        tmp += abs(old[i] - approx[i])
    flag = (tmp <= 10**(-16))
print("After {} steps of Zeidel algorithm we acquired approximate solution \n {}".format(num, approx))
