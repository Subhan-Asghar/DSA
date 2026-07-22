class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count=0
        for num in range(1,n+1):
            if n%num==0:
                count+=1
            if count==k:
                return num
        return -1