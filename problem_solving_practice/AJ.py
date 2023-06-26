s = [int(x) for x in input().split()]
w, h, x, y, r = s[0], s[1], s[2], s[3], s[4]

if x - r < 0 or y - r < 0 or x + r > w or y + r > h:
    print('No')
else:
    print('Yes')