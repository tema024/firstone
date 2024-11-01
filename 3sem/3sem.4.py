def triangle(size, symb):
    for i in range(1, ((size+1)//2) + 1):
        print(symb * i)
    if size % 2 == 0:
       for i in range((size+1)//2 , 0, -1):
        print(symb * i)
    else:
        for i in range(((size+1)//2) -1, 0, -1):
            print(symb * i)

size = int(input())
symb = input()

triangle(size,symb)