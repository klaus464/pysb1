x = 0
y = 1
n = int(input())

for z in range(1, n):
    n = x + y
    x = y
    y = n

print(n)
