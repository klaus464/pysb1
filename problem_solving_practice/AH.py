s = [int(x) for x in input().split()]
a, b, c = s[0], s[1], s[2]

if a < b and b < c:
    print('Yes')
else:
    print('No')