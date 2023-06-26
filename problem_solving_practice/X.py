num = int(input())

def check_for(n: int):
    if num%n == 0:
        print('Yes')
    else:
        print('No')

check_for(2)
check_for(4)
check_for(8)