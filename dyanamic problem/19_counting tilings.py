import sys
sys.setrecursionlimit(10**9)
n,m=list(map(int,input().split()))

dp={}
def twilling(i,j,mask):
    if j==m:
        return twilling(i+1,0,mask)
    if i==n:
        return 1 if mask==(1<<m)-1 else 0
    if (i,j,mask) in dp:
        return dp[(i,j,mask)]
    dp[(i,j,mask)]=0
    ans = 0
    
    if i>0 and (mask & 1==0):  # If we can place a vertical tile
        ans += twilling(i, j + 1, (mask >> 1) | (1 << (m - 1)))
    else:
        ans += twilling(i, j + 1, mask >> 1)  # SKIP THE CELL
        if j > 0 and ((mask & (1 << (m - 1)))==0):  # Place a horizontal tile
            ans += twilling(i, j + 1, (mask >> 1) | (1 << (m - 1)) | (1 << (m - 2)))
    dp[(i, j, mask)] = ans
    return dp[(i,j,mask)]%(10**9+7)
print(twilling(0,0,0))