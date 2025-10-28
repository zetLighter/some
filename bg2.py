import math


while True:
    value = (input("Введите неизвестную величину: "))
    a = 2.3
    try:
        value = float(value)
        if value < 1:
            result = 1.5*(math.cos(value))**2
        elif value == 1:
            result = 1.8*a*value
        elif value > 1:
            result = (value-2)**2+a
        print(result)
    except ValueError:
        print("Неправильный ввод")
