import math
import string


isDo = True
while isDo:
    result = 0
    x = input("Введите неизвестную величину x: ")
    if x.lower() == "завершить":
        isDo = False
    else:
        try:
            x = float(x)
            if x < 1:
                result = x*math.sin(x)**2
            elif x==1:
                result = math.sqrt(x**2+15)
            elif x>1:
                result = math.e**x
            print("Результат: " + str(result))
        except ValueError:
            print("Некорректный ввод!")

