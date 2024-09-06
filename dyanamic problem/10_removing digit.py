n = int(input())
dp = [float('inf')] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    a = str(i)  # Convert the current number to a string
    for c in a:
        digit = int(c)  # Convert each character back to an integer
        if digit != 0:
            dp[i] = min(dp[i], dp[i - digit] + 1)  # Update dp[i] using the minimum steps

print(dp[n])
