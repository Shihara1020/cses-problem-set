import sys
sys.setrecursionlimit(10**5)
x,n=list(map(int,input().split()))
list1=list(set(map(int,input().split())))
dp={}
def dfs(i,target):
    if target>n:
        return 0
    if target==n:
        return 1
    if i>=x:
        return 0
    if (i,target) in dp:
        return dp[(i,target)]
    dp[(i,target)]=dfs(i,target+list1[i])+dfs(i+1,target)
    return dp[(i,target)]

print(dfs(0,0)%(10**9+7))