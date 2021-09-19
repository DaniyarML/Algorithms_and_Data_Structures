# A robot is located at the starting point(0,0) and it needs to reach the mxn point.
# Robot can move to the bottom or to the right
# how many unique pathes to the point. Grid have coins. maximize the profit
# given a grid

# Time complexity: m*n
# Space complexity: m*n
# F(i,j) = F(i,j-1)+F(i-1,j)


def unique_path(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]

    for i in range(m):
        for j in range(n):
            if i-1>=0 and j-1>=0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])+grid[i][j]
            elif i-1>=0:
                dp[i][j] = dp[i-1][j]+grid[i][j]
            elif j-1>=0:
                dp[i][j] = dp[i][j-1]+grid[i][j]

    return dp[m-1][n-1]

grid = [[1,3,1,1],[2,1,1,1],[2,3,4,5]]

print(unique_path(grid))