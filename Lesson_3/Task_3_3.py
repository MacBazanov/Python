def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        print("аргументы должны быть числами")


print(f"Сумма двух наибольших аргументов:{my_func(3, 13, 8)}")
