lst = []

n = int(input())

while n != 0:
    lst.append(n)
    n = int(input())

for x in range(len(lst)):
    print('Case ' + str(x+1) + ': ' + str(lst[x]))