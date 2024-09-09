n=int(input())
a=list(map(int,input().split()))
sumt=sum(a)
dp=[[False]*(sumt+1) for _ in range(n+1)]
dp[0][0]=True
for i in range(1,n+1):
    val=a[i-1]
    for j in range(sumt+1):
        dp[i][j]=dp[i-1][j]
        if j>=val:
            dp[i][j]=dp[i][j] or dp[i-1][j-val]
print(dp[n].count(True)-1)
for i in range(1,len(dp[n])):
    if dp[n][i]==True:
        print(i,end=" ")






