#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# №2 В-13 В списке, состоящем из вещественных элементов, вычислить:
#  1) количество элементов списка, равных 0;
#  2) сумму элементов списка, расположенных после минимального элемента.
#  Упорядочить элементы списка по возрастанию модулей элементов.

import sys
import math

if __name__ == '__main__':
    A = list(map(float, input().split()))
    A_0 = 0
    n = 0

    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    for i in A:
        if i == 0:
            A_0 += 1

    for i, a in enumerate(A):
        if a < A[n]:
            n = i

    s = sum(A[n+1:])
    A = sorted(A, key=lambda y: math.fabs(y))

    print(f"Отсортированный список: {A}\nКоличество нулей: {A_0}\nСумма: {s}")
