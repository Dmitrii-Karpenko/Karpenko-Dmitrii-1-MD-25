def ex1():
    numbers = [10, 25, 37, 42, 55]
    user_number = int(input("Введите число:"))

    if user_number in numbers:
        print("Поздравляю, вы угадали число!")
    else:
        print("Нет такого числа!")

print(ex1())

def ex2():
    number = [1, 5, 10, 5, 6, 10, 11 ]
    count_dict = {}
    for i in number:
        if i in count_dict:
            print(f"Повторяющийся элемент: {i}")
        else:
            count_dict[i] = 1

print (ex2())

def ex3():