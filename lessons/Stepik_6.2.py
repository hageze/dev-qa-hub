city1, city2, city3 = input(), input(), input()
len1, len2, len3 = len(city1), len(city2), len(city3)

if len1 < len2 and len1 < len3:
    shortest = city1
elif len2 < len1 and len2 < len3:
    shortest = city2
else:
    shortest = city3

if len1 > len2 and len1 > len3:
    longest = city1
elif len2 > len1 and len2 > len3:
    longest = city2
else:
    longest = city3

print(shortest)
print(longest)