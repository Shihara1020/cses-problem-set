n,m=list(map(int,input().split()))
a=list(map(int,input().split()))
dp={}
def riders(weight,mask):
    if mask==(1<<n)-1:
        return 1
    if (weight,mask) in dp:
        return dp[(weight,mask)]
    ans=10**9
    for j in range(n):
        if mask&(1<<j)==0 and a[j]+weight<=m:
            ans=min(ans,riders(weight+a[j],mask|(1<<j)))
        if  mask&(1<<j)==0 and a[j]+weight>m:
            ans=min(ans,riders(a[j],mask|(1<<j))+1)
    dp[(weight,mask)]=ans
    return ans
print(riders(0,0))
