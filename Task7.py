number = int(input("Введіть 4-х значне число (наприклад, 1234): "))
n = abs(number)
digit1 = n // 1000 
n = n % 1000 
digit2 = n // 100 
n = n % 100
digit3 = n // 10 
n = n % 10
digit4 = n 
print("Цифри числа:")
print(digit1)
print(digit2)
print(digit3)
print(digit4)