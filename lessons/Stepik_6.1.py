num = int(input())
c1 = num // 100
c2 = (num // 10) % 10
c3 = num % 10
mx = max(c1, c2, c3)
mn = min(c1, c2, c3)
mid = (c1 + c2 + c3) - mx - mn
if mx - mn == mid:
    print("Число интересное")
else:
    print("Число неинтересное")
