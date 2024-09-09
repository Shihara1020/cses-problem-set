MOD = 1000000007

def solve(n):
    dp = [[0] * 2 for _ in range(n + 1)]
    
    # Base cases
    dp[n][0] = 1
    dp[n][1] = 1
    
    # Fill dp array
    for i in range(n - 1, -1, -1):
        dp[i][0] = (2 * dp[i + 1][0] + dp[i + 1][1]) % MOD
        dp[i][1] = (4 * dp[i + 1][1] + dp[i + 1][0]) % MOD
    
    # Final result
    return (dp[1][0] + dp[1][1]) % MOD

# Read input
t = int(input())
for _ in range(t):
    n = int(input())
    print(solve(n))
