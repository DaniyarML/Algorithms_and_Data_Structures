# You are climbing a stair case. it takes n steps to reach to the top.
# Each time you can climb k steps with red stairs where you are not allowed to step
# in how many distinct ways you climb to the top

def climb(n:int, k:int, stairs:list) -> int:
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, k+1):
            if i < j:
                break
            if stairs[i-1]:
                dp[i] = 0
            else:
                dp[i] += dp[i - j]

    return dp[n]

n = int(input())
k = int(input())
stairs = list(map(int, input().split(' ')))

print(climb(n,k,stairs))
