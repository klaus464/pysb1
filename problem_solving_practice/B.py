s = [int(x) for x in input().split()]

a, b, c = s[0], s[1], s[2]

if a + b > c and b + c > a and c + a > b:
    print("Yes")
else:
    print("No")