input()
lst = [int(x) for x in input().strip().split()]

sum = 0
for x in lst:
    if x & 1 == 1:
        sum += x

print(sum)