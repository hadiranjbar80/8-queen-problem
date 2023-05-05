import numpy as np
import queens_puzzle as qp

n = int(input('Enter a numebr!'))

mat = np.zeros((n,n),int)
ones=[]
xes = []
yes = []

for x in range(len(mat)):
    for y in range(len(mat)):
        qp.put(x,y,mat,ones,xes,yes)



print(mat)