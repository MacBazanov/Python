"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
num_n = int(input("Введите число n:"))num_n = int(input("Введите число n:"))
term_a = str(num_n)
term_b = str(num_n + num_n)
term_c = str(num_n + num_n + num_n)
sum = term_a + term_b + term_c
print(f"Сумма чисел n + nn + nnn: {int(sum)}")
