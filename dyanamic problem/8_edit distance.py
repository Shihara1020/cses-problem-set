n1=input()
n2=input()
def minDistance(word1,word2):
    n=len(word1)
    m=len(word2)
    dp=[[0]*(n+1) for i in range(m+1)]
    for i in range(n+1):
        dp[0][i]=i
    for j in range(m+1):
        dp[j][0]=j
    for i in range(1,len(word2)+1):
        for j in range(1,len(word1)+1):
            if word2[i-1]==word1[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    return dp[m][n]
print(minDistance(n1,n2))