with open('input.txt', 'r') as file:
    text = file.read()

endings = ['.', '!', '?']
number = 0
b = False

for char in text:
    if char.isalpha():
        b = True
    elif char in endings and b:
        number += 1
        b = False

print(number)
