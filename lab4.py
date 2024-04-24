def ex1(number):
    if number % 3 == 0:
        return True
    else:
        return False
print(ex1(3))
def ex2(number):
        try:
            result = 100 / number
            return result
        except ValueError:
            return "Ошибка: Введите число, а не строку!"
        except ZeroDivisionError:
            return "Ошибка: Нельзя делить на 0!"
print(ex2(0))
def ex3(date):
    day, month, year = map(int, date.split('.'))
    return day * month == year % 100

userdate = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if ex3(userdate):
    print("Эта дата является магической! ")
else:
    print("Эта дата не является магической. Попробуйте другую! ")
print (ex3())

