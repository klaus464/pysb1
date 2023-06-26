s = [int(x) for x in input().split()]
s.sort()

lst = []

while not (s[0] == 0 and s[1] == 0) :
    lst.append(s)
    s = [int(x) for x in input().split()]
    s.sort()

for x in lst:
    print(x[0], x[1])
