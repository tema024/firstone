A = list(map(int, input().split()))
o = []
for item in A:
    if A.count(item) == 1:
       o.append(item)
print (o)