def input(file):
    with open(file, 'r') as file:

        numbers = list(map(float, file.readline().strip().split()))
        operation = file.readline().strip()
    return numbers, operation

def operation(numbers, operation):
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        return numbers[0] - sum(numbers[1:])
    elif operation == '*':
        result = 1
        for number in numbers:
            result *= number
        return result

def output(file, result):
    with open(file_path, 'w') as file:
        file.write(str(result))


def main():
    numbers, operation = input('input.txt')
    result = operation(numbers, operation)
    output('output.txt', result)