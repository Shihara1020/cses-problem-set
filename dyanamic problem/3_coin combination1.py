import sys
sys.setrecursionlimit(10**9)
x,n=list(map(int,input().split()))
list1=list(map(int,input().split()))
dp={}
def dfs(target):
    if target>n:
        return 0
    if target==n:
        return 1
    if target in dp:
        return dp[target]
    dp[target]=0
    for i in list1:
        dp[target]+=dfs(target+i)
    return dp[target]

print(dfs(0)%(10**9+7))

