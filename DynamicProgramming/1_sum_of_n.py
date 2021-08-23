# Find the sum of the first n numbers
# What is the sum of 1 to n: n = 5: 1+2+3+4+5=15

def sum_of_n(n: int) -> int:
    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+i

    return dp[-1]

n = int(input())
print(sum_of_n(n))