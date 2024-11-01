N = int(input())
b = int(input())
c = int(input())
N_str = str(N)
l = len(N_str)
value_in_ten = 0
for i in range(l):
    value_in_ten += int(N_str[i]) * (b**(l-i-1))
if value_in_ten == 0:
    res = '0'
else:
    res = []
    while value_in_ten > 0:
        res.append(str(value_in_ten % c))
        value_in_ten = value_in_ten // c
    res = ''.join(res[::-1])
print (res)