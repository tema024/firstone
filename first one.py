x = int(input())
y = int(input())
with open('in.txt', 'w') as f_in, open('out.txt', 'w') as f_out:
   f_in.write(f'{x} {y}')
   f_out.write(f'{x-y}')