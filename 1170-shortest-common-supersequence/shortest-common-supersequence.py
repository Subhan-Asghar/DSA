class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m=len(str2)
        n=len(str1)
        dp=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    top=dp[i-1][j]
                    prev=dp[i][j-1]
                    dp[i][j]=max(top,prev)
        i=n
        j=m
        result=[]
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                result.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:

                result.append(str1[i-1])
                i-=1
            else:
                result.append(str2[j-1])
                j-=1
        while i >0:
            result.append(str1[i-1])
            i-=1
        while j>0:
            result.append(str2[j-1])
            j-=1
            
        return "".join(result[::-1])
    
        