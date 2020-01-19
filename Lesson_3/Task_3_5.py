def sum_nums():
    mode_of = False
    total_result = 0
    while mode_of == False:

        string = input('ВВведите числа, разделённые пробелами или нажмите "q", чтобы выйти:').split()
        result = 0
        i = 0
        while i < len(string):
            if string[i] == "q":
                mode_of = True
                break
            else:
                result += int(string[i])
                i += 1
        total_result += result
        print(f"сумма чисел равна: {total_result}")
    print(f"Вы вышли из программы. Итоговая сумма чисел равна: {total_result}")


sum_nums()