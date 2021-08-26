# You are climbing a stair case. it takes n steps to reach to the top. Also you have
# a cost to step any stair which is given within P list
# Each time you can climb k steps
# Find the way to reach the top with minimal cost

# Define objective function: F(i) ...
# Identify the base case: F(0) = 0, F(1) = P[0], F(2) = min(F(1),F(2))
# Write down the transition function: F(n) = P(n) + min(F(n-1), F(n-2))
# In which way we gonna solve:Bottom-up
# Where to look for the answer: F(n)

#Time complexity: O(n)
#Space complexity: O(n)
def climb(n: int, k: int, P: list) -> int:
    dp = [0]*(n+1)

    for i in range(1, n+1):
        dp[i] = P[i-1] + min(dp[max(i-k,0):i])
    print(dp)
    return dp[n]

print(climb(6, 3, [3, 2, 5, 1, 5, 3]))

#Time complexity: O(n)
#Space complexity: O(k)

def climb(n: int, k: int, P: list):
    dp = [0]*k

    for i in range(1, n+1):
        dp[i%k] = P[i-1]+min(dp[:i])

    return dp[n%k]

print(climb(6, 3, [3, 2, 5, 1, 5, 3]))
