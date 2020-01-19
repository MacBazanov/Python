def division(arg_1, arg_2):
    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        result = arg_1 / arg_2
    except ValueError:
        return "Выдолжны вводить число! Перезапустите программу"
    except ZeroDivisionError:
        return "на ноль делить нельзя! Перезапустите программу"
    return result


num_1 = input("Введите делимое:")
num_2 = input("Введите делитель:")
print(f"Результат деления: {division(num_1, num_2)}")
