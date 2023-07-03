input()
lst = [int(x) for x in input().strip().split()]
lst.reverse()
print(*lst)