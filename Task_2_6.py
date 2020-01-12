# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
print ("Добро пожаловать в программу 'Товары'")
mode = "да"
devices = []
analys_name = []
analys_price = []
analys_device_count = []
analys_unit = []
analys = {}
key = 0
i = 1
while mode.lower() == "да":
    name = input("Введите название устройства:")
    price = input("Введите цену устройства:")
    device_count = input("Введите количество устройств:")
    unit = input("Введите единицу измерения:")
    devices.append(i)
    devices.append({"название": name, "цена": price, "количество": device_count, "ед": unit})
    mode = input("Хотите ввести еще данные (да/нет):")
    analys_name.append(name)
    analys_price.append(price)
    analys_device_count.append(device_count)
    analys_unit.append(unit)
    i +=1
devices = tuple(devices)
print(f"Структура: {devices}")
analys = {"название": analys_name, "цена": analys_price, "количество": analys_device_count, "ед": analys_unit }
print(f"Аналитика: {analys}")
















