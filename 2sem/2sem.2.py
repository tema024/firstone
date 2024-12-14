l = input().split()
x = int(l[0])
A = list(l[1])
s=str()
for i in range(0, len(A)-x+1,x):
    A[i:i + x] = A[i:i + x][::-1]
for i in A:
    s += i
print(s)
