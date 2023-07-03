t = int(input())

while t != 0:
    x = int(input())
    result = ''
    while not (x == 0 or x == 1):
        result += str(x % 2)
        x //= 2
    result += str(x)
    print(result[::-1])
    t -= 1