def ex1():
    N = int(input("Сколько слов вы хотите ввести: "))
    result = ""
    for i in range(N):
        word = input("Введите слово: ")
        if i == N-1:
            result += word
        else:
            result += word + " "
    print("Результат:", result)
print(ex1())

def ex2():
    result = ""
    word = ""

    while word != "stop":
        word = input("Введите слово (для завершения введите 'stop'): ")
        if word != "stop":
            result += word + " "

    print("Результат:", result.strip())
print(ex2())
def ex3():
    word = input("Введите слово: ")

    if 'ф' in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")
print(ex3())