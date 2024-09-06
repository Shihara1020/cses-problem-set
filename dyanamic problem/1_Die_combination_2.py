n=int(input())
dp=[0 for _ in range(n+1)]
dp[0]=1
for i in range(1,n+1):
    for j in range(1,7):
        if (j<=i):
            dp[i]+=dp[i-j]
print(dp[n]%(10**9+7))