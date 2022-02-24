def list(products):
    if products:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Продукт",
                "Магазин",
                "Цена"
            )
        )
        print(line)

        for idx, product in enumerate(products, 1):
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    idx,
                    product.get('name', ''),
                    product.get('shop', ''),
                    product.get('price', 0)
            )
        )
        print(line)
