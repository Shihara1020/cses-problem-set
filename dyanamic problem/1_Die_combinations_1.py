import sys
sys.setrecursionlimit(10**9)
n=int(input())
chashe={}
def dfs(target):
    if target==n:
        return 1
    if target in chashe:
        return chashe[target]
    if target>n:
        return 0
    chashe[target]=0
    for i in range(1,7):
        chashe[target]+=dfs(target+i)
    return chashe[target]%(10**9+7)
print(dfs(0))
