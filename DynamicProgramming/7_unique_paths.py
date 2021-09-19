# A robot is located at the starting point(0,0) and it needs to reach the mxn point.
# Robot can move to the bottom or to the right
# how many unique pathes to the point
# given m and n

# Time complexity: m*n
# Space complexity: m*n
# F(i,j) = F(i,j-1)+F(i-1,j)
def unique_pathes(m: int, n: int) -> int:
    dp = [[0]*n for i in range(m)]

    dp[0][0] = 1

    for i in range(0, m):
        for j in range(0, n):
            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = dp[i][j-1]+dp[i-1][j]
            elif i - 1 >= 0:
                dp[i][j] = dp[i-1][j]
            elif j - 1 >= 0:
                dp[i][j] = dp[i][j-1]
    print(dp)
    return dp[m-1][n-1]


print(unique_pathes(3,4))


# with ob
def