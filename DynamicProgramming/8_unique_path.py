# A robot is located at the starting point(0,0) and it needs to reach the mxn point.
# Robot can move to the bottom or to the right
# how many unique pathes to the point. Grid have obstacles
# given a grid

# Time complexity: m*n
# Space complexity: m*n
# F(i,j) = F(i,j-1)+F(i-1,j)


def unique_path(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dp[i][j] = 0
                continue

            if i-1 >= 0 and j-1 >= 0:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            elif i-1 >= 0:
                dp[i][j] = dp[i-1][j]
            elif j-1 >= 0:
                dp[i][j] = dp[i][j-1]

    print(dp)
    return dp[m-1][n-1]

grid = [[0,0,0,0],[0,0,1,1],[0,0,0,0]]
print(unique_path(grid))