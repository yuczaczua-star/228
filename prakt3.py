while True:
    try:
        n = int(input("Введите число N: "))

        for i in range(1, n + 1):
            if str(i) == str(i)[::-1]:

                print(i)
    except Exception:
        print("НЕ-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-Е-ЕТ")