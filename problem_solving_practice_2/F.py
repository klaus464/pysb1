input()
lst = [int(x) for x in input().strip().split()]
lst.sort()

for x in range(len(lst)):
    if lst[x] == lst[x+1]:
        print(lst[x])
        exit()