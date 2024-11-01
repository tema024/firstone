a = list(map(int, input().split()))
a[0 : len(a) - 1], a[len(a) - 1 : len(a)] = a[len(a) - 1 : len(a)], a[0 : len(a) - 1]
print(a)
