n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

# dp[money] represents the maximum pages we can get with exactly 'money' amount spent
dp = [0] * (x + 1)

# Iterate over each book
for i in range(n):
    # Iterate backwards to avoid overwriting current dp values prematurely
    for money in range(x, prices[i] - 1, -1):
        dp[money] = max(dp[money], dp[money - prices[i]] + pages[i])

# The maximum value for dp[x] is the answer
print(dp[x])

