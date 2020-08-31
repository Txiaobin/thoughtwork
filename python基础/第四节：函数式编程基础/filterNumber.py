import numpy as np

def filterNumber(n, iter):
    result = []
    for i in range(np.size(iter, 0)):
        if iter[i,-1] > n:
            result.append(iter[i,:])
    return result


iter = np.array([['ITEM000001', 5], ['ITEM000003', 2], ['ITEM000005', 3]])
n = '5'
print(filterNumber(n, iter))