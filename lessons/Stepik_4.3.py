a = int(input())
b = int(input())
op = input()
if (op == "/") and (b == 0):
    print('На ноль делить нельзя!')
elif op != "+" and op != "-" and op != "*" and op != "/":
    print("Неверная операция")
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "+":
    print(a + b)
elif op == "-":
    print(a - b)