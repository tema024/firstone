A = list(map(int, input().split()))
for i in range(int(len(A) / 2)): A[2*i], A[2*i + 1] = A[2*i + 1], A[2*i]
print (A)