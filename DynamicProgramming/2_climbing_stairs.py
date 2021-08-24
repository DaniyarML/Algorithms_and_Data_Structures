# You are climbing a stair case. it takes n steps to reach to the top.
# Each time you can climb 1 or 2 steps
# in how many distinct ways you climb to the top

def climb(n: int) -> int:
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    return dp[-1]

# n = int(input())
#print(climb(n))

#optimize space complexity

def climb(n: int) -> int:
    a = 1
    b = 1

    for i in range(2, n+1):
        c = a + b
        a = b
        b = c

    return c

# n = int(input())
# print(climb(n))

# Each time you can climb 1, 2 or 3 steps
# in how many distinct ways you climb to the top


def climb(n: int) -> int:
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

    return dp[n]

n = int(input())
print(climb(n))


