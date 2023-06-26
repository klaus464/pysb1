s = [int(x) for x in input().split()]

v, e = s[0], s[1]

output = []

for i in range(v):
    x = [0 for y in range(e)]
    output.append(x)

for i in range(e):
    l = [int(x) for x in input().split()]
    output[l[0] - 1][i] = 1
    output[l[1] - 1][i] = 1
    
for x in output:
    for y in x:
        print(y, end=" ")
    print()