with open("in.txt", "r") as file:
    lines = file.readlines()
    numbers = list(map(int, lines[0].split()))
    op = lines[1].strip()

if op == "+":
    result = sum(numbers)
elif op == "-":
    result = numbers[0]
    for n in numbers[1:]:
        result -= n
elif op == "*":
    result = 1
    for n in numbers:
        result *= n

with open("out.txt", "w") as file:
    file.write(str(result))
