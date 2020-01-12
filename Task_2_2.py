first_list = list(input("Введите список элементов:"))
print(f"Первоначальный список: {first_list}")
i = 0
while i < len(first_list):
    change = first_list[i:i+2]
    change.reverse()
    first_list[i:i + 2] = change
    i += 2
print(f"Изменённый список    : {first_list}")

