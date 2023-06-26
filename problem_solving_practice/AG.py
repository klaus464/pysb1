s = [int(x) for x in input().split()]
a, b = s[0], s[1]

if a > b:
    print('a > b')
elif a < b:
    print('a < b')
else:
    print('a == b')