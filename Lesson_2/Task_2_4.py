# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
my_string = input("Введите строку из нескольких слов:")

split_string = list(my_string.split())
i = 0
while i < len(split_string):
    print(f"{i+1}. {split_string[i]:.10s}")
    i += 1





