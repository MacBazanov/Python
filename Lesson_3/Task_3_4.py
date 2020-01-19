def my_func(x, y):
    try:
        x = float(x)
        y = - int(y)
        my_abs = x ** y
        return my_abs
    except ValueError:
        return "Выдолжны вводить число! Перезапустите программу"


print(f"{(my_func(15, 3)):.7f}")
