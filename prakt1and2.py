import math

while True:
    try:
        x = float(input("Введите x: "))
        if x < 0:
            print("При отрицательном x функция не определена.")
            continue
        elif x == 0:
            print("При x = 0 происходит деление на ноль.")
            continue
        else:
            y = (-2 * math.sqrt(x + math.pi**2) * math.tan(math.pi)) / (x ** math.pi)
            print("y =", y)

            if y > 0:
                print("Значение положительное")
            elif y < 0:
                print("Значение отрицательное")
            else:
                print("Значение равно нулю")

            if y == int(y):
                if int(y) % 2 == 0:
                    print("Значение чётное")
                else:
                    print("Значение нечётное")
            else:
                print("Значение не целое — чётность не определяется")

            break

    except ValueError:
        print("Ошибка: введите корректное число.")
