#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# №1 В-1 Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым элементом.
# Преобразованный массив вывести.

import sys

if __name__ == '__main__':

    A = list(map(int, input().split()))
    x = 0

    if len(A) != 10:
        print("Неверный размер списка", file=sys.stderr)
        exit(1)

    k = list(i for i in range(len(A)) if A[i] == max(A))
    k = k[0]

    A[0], A[k] = A[k], A[0]
    print(A)
