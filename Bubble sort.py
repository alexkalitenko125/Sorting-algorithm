# -*- coding: utf-8 -*-
"""
Сортировка пузырьком
"""


a = list(map(int,input().split()))

n = len(a)

for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]  


print(a)                

