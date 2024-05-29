def ex3():
    total = 0
    print("Нужно купить:")
    with open('products.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            product, quantity, price = line.strip().split(',')
            total += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total} руб.")
