n = int(input())
k = n
arr = []
i = 2
while i <= k/2:
    if n % i == 0:
        arr.append(i)
        n = n / i
    else:
        i = i + 1
if arr == []:
    print (k)
else:
    print (arr)