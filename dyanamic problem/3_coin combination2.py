x,n=list(map(int,input().split()))
list1=list(map(int,input().split()))

dp=[0 for _ in range(n+1)]
dp[0]=1
for i in range(1,n+1):
    for j in range(len(list1)):
        if list1[j]<=i:
            dp[i]+=dp[i-list1[j]]
print(dp[n]%(10**9+7))