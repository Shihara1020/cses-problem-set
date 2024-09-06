import sys
sys.setrecursionlimit(10**9)
numbers,sumt=list(map(int,input().split()))
list1=list(set(map(int,input().split())))
list1.sort(reverse=True)
dp={}
def dfs(i,target):
    if target==sumt:
        return 0
    if i==len(list1):
        return float('inf')
    if target>sumt:
        return float("inf")
    if (i,target) in dp:
        return dp[(i,target)]
    dp[(i,target)]=min(dfs(i,target+list1[i])+1,dfs(i+1,target))
    return dp[(i,target)]
k=dfs(0,0)
if k==float('inf'):
    print(-1)
else:
    print(k)