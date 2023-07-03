input()
lst = [int(x) for x in input().strip().split()]

output = []
for x in lst:
    if lst.count(x) == 1:
        output.append(x)
print(*output)