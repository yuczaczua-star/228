import sys

try:

    x = float(input("Введите начальное количество тонн X: "))
    if x < 0:
        sys.exit(1)
    n = int(input("Введите количество лет N: "))
    if n < 0:
        sys.exit(1)
    god = 0

    while god < n:
        x = x + x * 0.1
        god = god + 1

    print("Через", n, "лет будет", round(x, 2), "тонн")

except Exception:
    print ("Ашибка однако")
