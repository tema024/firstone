def conv(N, b, c):
    dv = 0
    for i, digit in enumerate(reversed(N)):
        dv += int(digit) * (b ** i)
    if dv == 0:
        return '0'
    result = ''
    while dv > 0:
        result = str(dv % c) + result
        dv //= c

    return result
N = input()
b = int(input())
c = int(input())

print(conv(N, b, c))