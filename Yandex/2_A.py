import math

def calc_dist(x1, y1, x2, y2):
    return math.sqrt(((x2-x1)**2+(y2-y1)**2))

n = int(input())

for i in range(n):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    AB = calc_dist(x1, y1, x2, y2)
    CD = calc_dist(x3, y3, x4, y4)
    AC = calc_dist(x1, y1, x3, y3)
    BD = calc_dist(x2, y2, x4, y4)
    AD = calc_dist(x1, y1, x4, y4)
    BC = calc_dist(x2, y2, x3, y3)
    #print(AB, CD, AC, BD, AD, BC)
    if (AB == CD and AC == BD) or (AB == CD and AD == BC) or (AC == BD and AD == BC):
        print('YES')
    else:
        print('NO')
