import sys
sys.setrecursionlimit(10**9)
n=int(input())
graphy=[]
for _ in range(n):
    graphy.append(input())
dp={}
def dfs(i,j):
    if i==0 and j==0:
        return 0
    if i==0:
        for k in range(0,j):
            if graphy[0][k]=="*":
                return 0
        return 1
    if j==0:
        for k in range(0,i):
            if graphy[k][0]=="*":
                return 0
        return 1
    
    if (i,j) in dp:
        return dp[(i,j)]
    
    if graphy[i-1][j]=="*" and graphy[i][j-1]=="*":
        return 0
    if graphy[i][j-1]=="*":
        dp[(i,j)]=dfs(i-1,j)
    if graphy[i-1][j]=="*":
        dp[(i,j)]=dfs(i,j-1)
    if graphy[i-1][j]!="*" and graphy[i][j-1]!="*":
        dp[(i,j)]=dfs(i-1,j)+dfs(i,j-1)
    return dp[(i,j)]
if graphy[n-1][n-1]=="*":
    print(0)
elif n==1 and graphy[0][0]=="*":
    print(0)
elif n==1 and graphy[0][0]==".":
    print(1)
else:
    print(dfs(n-1,n-1)%(10**9+7))