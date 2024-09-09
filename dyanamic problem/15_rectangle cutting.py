a,b=list(map(int,input().split()))
dp=[[10**9]*(b+1) for _ in range(a+1)]

for i in range(1,a+1):
    for j in range(1,b+1):
        if i==j:
            dp[i][j]=0
        else:
            #horizontal cut
            for h in range(1,i):
                dp[i][j]=min(dp[i][j],dp[h][j]+dp[i-h][j]+1)
            
            #vertical cut
            for k in range(1,j):
                dp[i][j]=min(dp[i][j],dp[i][k]+dp[i][j-k]+1)
print(dp[a][b])  