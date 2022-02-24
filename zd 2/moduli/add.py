def add():
    name = input("Название продукта: ")
    shop = input("Название магазина: ")
    price = float(input("Стоимость: "))
    products = {
        'name': name,
        'shop': shop,
        'price': price,
    }
    return products