from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count=[Counter(x) for x in strs]
        memo={}
        def knapsack(M,N,i):
            if i==0:
                return 0
            if (M,N,i) in memo:
                return memo[(M,N,i)]
            if count[i-1]["0"]>M or count[i-1]["1"]>N:
                ans=knapsack(M,N,i-1)
            else:
                take=1+knapsack(M-count[i-1]['0'],N-count[i-1]["1"],i-1)
                skip=knapsack(M,N,i-1)
                ans=max(take,skip)
            memo[(M,N,i)]=ans
            return ans
        return knapsack(m,n,len(strs))
