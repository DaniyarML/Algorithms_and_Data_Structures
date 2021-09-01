a = int(input())
b = int(input())
c = int(input())
d = int(input())


if c == 0 and d == 0:
    print('INF')

elif b % a != 0:
    print('NO')

elif b % a == 0:
    print(b//a)



