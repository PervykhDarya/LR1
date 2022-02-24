#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from moduli import add, list, help, select


if __name__ == '__main__':
    products = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            products.append(add.add())

        elif command == 'list':
            list.list(products)

        elif command.startswith('select '):
            select.select(products)

        elif command == 'help':
            products.append(help.help())

        else:
            print(f"Неизвестная команда {command}")