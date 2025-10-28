while True:
    try:
        count = int(input("Введите число в диапазоне 20-40: "))
        if count < 20 or count > 40:
            print("Введеное число не попадаюет в диапозон")
        else:
            if count == 20 or count > 24 and count < 31 or count > 34 and count < 41:
                print("Вам " + str(count) + " лет")
            elif count == 21 or count == 31:
                print("Вам " + str(count) + " год")
            else:
                print("Вам " + str(count) + " года")
    except ValueError:
        print("Некорректное значение!")




