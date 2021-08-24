# You are climbing a stair case. it takes n steps to reach to the top.
# Each time you can climb k steps
# in how many distinct ways you climb to the top

def climb(n: int, k: int) -> int:
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        for j in range(1, k+1):
            if i < j:
                break
            dp[i] += dp[i-j]

    return dp[n]

n = int(input())
k = int(input())
print(climb(n, k))


