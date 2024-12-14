def fib(n):
    mem = [-1] * (n + 1)
    def help(x):
        if mem[x] != -1:
            return mem[x]
        if x == 0:
            mem[x] = 0
        elif x == 1:
            mem[x] = 1
        else:
            mem[x] = help(x - 1) + help(x - 2)
        return mem[x]

    return help(n)

n = int(input())
res = fib(n)
print(res)
