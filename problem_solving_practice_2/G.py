temp = [int(x) for x in input().split()]
key = temp[1]

lst = [int(x) for x in input().split()]

try:
    x = lst.index(key)
    print(x)
except ValueError:
    print(-1)
