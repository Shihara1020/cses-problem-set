import sys
sys.setrecursionlimit(10**9)
n,x=list(map(int,input().split()))
prices=list(map(int,input().split()))
pages=list(map(int,input().split()))
zipped=list(zip(prices,pages))
dp={}
def dfs(i,money):
    if i==n:
        return 0
    if (i,money) in dp:
        return dp[(i,money)]
    skipped=dfs(i+1,money)
    select=0
    if zipped[i][0]+money<=x:
        select=dfs(i+1,money+zipped[i][0])+zipped[i][1]
    dp[(i,money)]=max(skipped,select)
    return dp[(i,money)]
print(dfs(0,0))

