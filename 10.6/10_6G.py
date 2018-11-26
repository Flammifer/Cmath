import numpy as np

#matrix input

a=10

dimension = 100

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
#print(A)

#direct
tmp = []
for i in range(dimension):
    for j in range(i+1,dimension):
        for k in range(dimension+1):
            tmp.append(np.subtract(A[j][k], np.multiply(A[j][i], np.divide(A[i][k], float(A[i][i])))))
        A[j] = tmp
        tmp = []
    tmp = []

#reverse

for i in range(dimension-1, -1, -1):
    for j in range(i-1, -1, -1):
        for k in range(dimension+1):
            tmp.append(np.subtract(A[j][k], np.multiply(A[j][i], np.divide(A[i][k], float(A[i][i])))))
        A[j] = tmp
        tmp = []
    tmp = []


solution = []
for i in range(dimension):
    solution.append(np.divide(A[i][dimension],A[i][i]))
print("According to Gauss method the solution is")
print(solution)
