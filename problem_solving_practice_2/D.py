t = int(input())

while t != 0:
    input()
    lst = [int(x) for x in input().strip().split()]
    sum = 0
    for x in lst:
        sum += x
    print(sum)
    t -= 1
    