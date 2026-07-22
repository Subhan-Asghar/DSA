class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        result=[]
        for num in range(1,n+1):
            if n%num==0:
                result.append(num)
        k=k-1
        if len(result)<=k:
            return -1
        return result[k] 