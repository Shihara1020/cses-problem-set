
MOD = 1000000007
mod_inverse_2 = 500000004

n = int(input())
if (n * (n + 1)) % 4 != 0:
    print(0)
else:
    maxSum = (n * (n + 1)) // 4
    dp = [[0] * (maxSum + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        val = i
        for j in range(maxSum + 1):
            dp[i][j] = dp[i - 1][j]
            if j - val >= 0:
                dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
    print((dp[n][maxSum] * mod_inverse_2) % MOD)

