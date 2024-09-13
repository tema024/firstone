def convert_from_base(number: str, base: int) -> int:
    """Конвертация числа из произвольной системы счисления в десятичную."""
    return int(number, base)

def convert_to_base(number: int, base: int) -> str:
    """Конвертация числа из десятичной системы в произвольную."""
    if number == 0:
        return "0"
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(str(x) for x in digits[::-1])

def perform_operation(numbers, operation):
    """Выполнение арифметической операции."""
    if operation == '+':
        return sum(numbers)
    elif operation == '-':
        return numbers[0] - sum(numbers[1:])
    elif operation == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
    else:
        raise ValueError("Unsupported operation")

def main():
    # Чтение данных из файла input.txt
    with open('input.txt', 'r') as file:
        numbers = file.readline().strip().split()  # Первая строка - числа
        operation = file.readline().strip()        # Вторая строка - операция
        base = int(file.readline().strip())        # Третья строка - основание системы счисления

    # Конвертируем числа из указанной системы счисления в десятичную
    decimal_numbers = [convert_from_base(num, base) for num in numbers]

    # Выполняем операцию
    result_decimal = perform_operation(decimal_numbers, operation)

    # Конвертируем результат обратно в исходную систему счисления
    result_base = convert_to_base(result_decimal, base)

    # Запись результата в файл output.txt
    with open('output.txt', 'w') as file:
        file.write(result_base)

if __name__ == "__main__":
    main()