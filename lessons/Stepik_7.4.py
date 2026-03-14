n = int(input())
f1 = 0
f2 = 1
total = 0
for i in range(n):
    total = f1 + f2
    f1, f2 = f2, f1 + f2
    print(f1, end=' ')