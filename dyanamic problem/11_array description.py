n,m=list(map(int,input().split()))
a=list(map(int,input().split()))

dp=[[0]*(m+1) for _ in range(n+1)]

for i in range(1,m+1):
    if a[0]==i or a[0]==0:
        dp[1][i]=1

for i in range(2,n+1):
    for j in range(1,m+1):
        if a[i-1]!=0 and a[i-1]!=j:
            dp[i][j]=0
        
        else:
            for prev in [j-1,j,j+1]:
                if 1<=prev<=m:
                    dp[i][j]+=dp[i-1][prev]
ans=0
for i in dp[n]:
    ans+=i
print(ans%(10**9+7))