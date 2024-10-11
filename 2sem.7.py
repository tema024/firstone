a = list(map(int, input().split()))
c = []
m = a[0]
for item in a:
    c.append(a.count(item))
    if a.count(item) == max(c):
       m = item
print (m)