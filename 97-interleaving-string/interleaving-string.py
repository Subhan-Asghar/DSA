from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n + m != len(s3):
            return False
        @cache
        def func(i,j,string):
            if i==n and j==m:
                return True
        
            if i<n and s1[i]==s3[i+j]: 
                if func(i+1,j,string+s1[i]):
                    return True
            if j<m and s2[j]==s3[i+j]:
                if func(i,j+1,string+s2[j]):
                    return True
            return False
        return func(0,0,"")

