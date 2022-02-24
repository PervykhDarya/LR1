def select_products(products):
    products = input("Введите товар: ")
    result = []
    for tovar in products:
        if tovar.get('name', ''):
            result.append(tovar)
    return result
