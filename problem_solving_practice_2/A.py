input()
lst = [int(x) for x in input().strip().split()]
lst.sort()

print(lst[-1])