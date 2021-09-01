# You are climbing a stair case. it takes n steps to reach to the top. Also you have
# a cost to step any stair which is given within P list
# Each time you can climb k steps
# Find the way to reach the top with minimal cost
# Reconstruct the path

# Define objective function: F(i) ...
# Identify the base case: F(0) = 0, F(1) = P[0], F(2) = min(F(1),F(2))
# Write down the transition function: F(n) = P(n) + min(F(n-1), F(n-2))
# In which way we gonna solve:Bottom-up
# Where to look for the answer: F(n)


def climb(n: int, k: int, P:list) -> list:
    dp = [0]*(n+1)
    path = [0]*(n+1)
    ans = []
    for i in range(1, n+1):
        for j in range(1,k+1):
            mini_val = 1e9
            mini_pos = 0
            for l in range(max(i-k, 0), i):
                if mini_val >= dp[l]:
                    mini_val = dp[l]
                    mini_pos = l

            dp[i] = P[i-1] + mini_val
            path[i] = mini_pos

    i = n
    while i != 0:
        ans.append(i)
        i = path[i]
    return ans[::-1]

print(climb(6, 3, [3, 2, 5, 1, 5, 3]))