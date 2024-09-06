n,sumt=list(map(int,input().split()))
list1=list(set(map(int,input().split())))
dp=[10**9 for _ in range(sumt+1)]
dp[0]=0
for i in range(1,sumt+1):
    for j in range(len(list1)):
        if (list1[j]<=i):
            dp[i]=min(dp[i],dp[i-list1[j]]+1)
k=dp[sumt]
if k>=10**9:

    print(-1)
else:
    print(k)