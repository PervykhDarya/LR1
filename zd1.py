# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

import fun


if __name__ == "__main__":
    figure_type = int(input("0 - прямоугольник, 1 - треугольник: "))
    a, b = input("Введите два параметра фигуры: ").split()
    print(fun.figure(figure_type)(int(a), int(b)))