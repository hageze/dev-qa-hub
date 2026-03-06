# Задача: Размножение n
# Вычисление суммы n + nn + nnn

n = int(input())

n1 = n
n2 = n * 10 + n
n3 = n * 100 + n * 10 + n

print(n1 + n2 + n3)