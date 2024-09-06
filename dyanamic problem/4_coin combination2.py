MOD=(10**9+7)
n, x = 3,9
a =[2,3,5]
    
dp = [[0] * (x + 1) for _ in range(n + 1)]
print(dp)
# dp[i][k] = number of ways to construct sum k
# such that all coins before coin[i] are unusable

for i in range(n):
    dp[i][0] = 1

for i in range(n - 1, -1, -1):
    for sum_value in range(1, x + 1):
        skipping = dp[i + 1][sum_value]
        picking = 0
        if a[i] <= sum_value:
            picking = dp[i][sum_value - a[i]]
        dp[i][sum_value] = (skipping + picking) % MOD

print(dp[0][x])
