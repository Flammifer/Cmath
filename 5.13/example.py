def f1(x):
    return x
def f2(x):
    return x+1
def f3(x):
    return x+2

func = []
func.append(f1)
func.append(f2)
func.append(f3)


def linear_combination(t, w): #вектор-функция
    result = []
    for x in t:
        tmp = 0
        for j in range(len(func)):
            tmp = w[j]*func[j](x)
        result.append(tmp)
    return result

print(linear_combination([1], [1, 1, 1]))    
