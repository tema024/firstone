import numpy as np

N = int(input())
M = int(input())

matrix = np.zeros((N,M), dtype = int)

top, bottom = 0, N-1
left, right = 0, M-1
n = 1
while top<=bottom and left<=right:
    for i in range(left,right + 1):
        matrix[top][i] = n
        n += 1
    top +=1
    for i in range(top,bottom+1):
        matrix[i][right] = n
        n += 1
    right -= 1
if top<=bottom:
    for i in range(right,left -1, -1):
        matrix[i][left] = n
        n += 1
    left += 1


print(matrix)