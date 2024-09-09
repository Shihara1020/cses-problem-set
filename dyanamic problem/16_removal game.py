n=int(input())
a=list(map(int,input().split()))
p=[0]*(n)
dp=[[0]*(n) for _ in range(n)]

for i in range(n):
    dp[i][i]=a[i] #length of array one
    if i==0:
        p[0]=a[i]
    else:
        p[i]=p[i-1]+a[i]
for length in range(2,n+1): #fill the length 2 to n
    for i in range(length-1,n):
        if i<length:
                total=p[i]
        else:
            total=p[i] - p[i - length]
        selectLast = total - dp[i - length + 1][i - 1]
        selectFirst = total - dp[i - length + 2][i]
        dp[i - length+ 1][i] = max(selectFirst, selectLast)

print(dp[0][n - 1])
