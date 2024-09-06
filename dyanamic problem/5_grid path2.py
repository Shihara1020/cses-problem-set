n=int(input())
graphy=[]
for _ in range(n):
    graphy.append(input())
dp=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graphy[0][0]=="*":
            dp[0][0]=0
        if graphy[0][0]==".":
            dp[0][0]=1
        if graphy[i][j]=="*":
            dp[i][j]=0
        elif i==0:
            dp[i][j]=dp[0][j-1]
        elif j==0:
            dp[i][j]=dp[i-1][0]
        else:
            dp[i][j]=dp[i-1][j]+dp[i][j-1]
print(dp[n-1][n-1]%(10**9+7))