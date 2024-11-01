def function(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x1, y1 = function(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return d, x, y

import sys
for line in sys.stdin:
    a, b = map(int, line.split())
    d, x, y = function(a, b)
    print(x, y, d)