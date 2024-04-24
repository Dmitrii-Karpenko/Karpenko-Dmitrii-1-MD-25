def ex1():
    password = input('Введите пароль')
    Repassword = input('Введите пароль повторно')
    if password == Repassword:
        print('Пароль принят')
    else:
        print('Пароль не принят')
print(ex1())

def ex2():
    nomer = input('введите номер вашего места')
    if int(nomer) <= 36 and int(nomer) % 2 == 0:
        print('Ваше место верхнее, купе')
    elif int(nomer) <= 36 and int(nomer) % 2 != 0:
        print('Ваше место нижнее, купе')
    elif int(nomer) > 36 and int(nomer) % 2 != 0:
        print('Ваше место боковое, верхнее')
    else:
        print('Ваше место боковое, нижнее')
print(ex2())

def ex3():
    year = input('ведите год')
    if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0:
        print('Год високосный')
    else:
        print('Это год не високосный')
print(ex3())
def ex4():
    color1 = input("Введите первый основной цвет: ")
    color2 = input("Введите второй основной цвет: ")
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        return "фиолетовый"
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        return "оранжевый"
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        return "зеленый"
    else:
        return "Ошибка: Введите только названия 'красный', 'синий' или 'желтый'."
print (ex4())