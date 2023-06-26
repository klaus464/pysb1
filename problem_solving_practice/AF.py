n = int(input())

s = n % 60
n = n // 60
m = n % 60
n = n // 60
h = n

print(str(h) + ':' + str(m) + ':' + str(s))