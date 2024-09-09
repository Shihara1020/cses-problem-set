n=int(input())
list1=[]
for _ in range(n):
    list1.append(list(map(int,input().split())))
list1.sort()
dp={}
def project(i,e):
    if i==n:
        return 0
    if (i,e) in dp:
        return dp[(i,e)]
    skip=project(i+1,e)
    select=0
    for j in range(i,n):
        if list1[j][0]>e:
            select=project(j,list1[j][1])+list1[j][2]
            break
    dp[(i,e)]=max(skip,select)
    return dp[(i,e)]
print(project(0,0))

    
