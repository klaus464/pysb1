s = [int(x) for x in input().split()]
a, b, c = s[0], s[1], s[2]

count = 0

for i in range(a, b+1):
    if c % i == 0:
        count+=1

print(count)
