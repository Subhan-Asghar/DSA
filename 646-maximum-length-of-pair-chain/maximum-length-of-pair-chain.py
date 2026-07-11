class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        def func(index,prev):
            if index==len(pairs):
                return 0
            if (index,prev) in memo:
                return memo[(index,prev)]
            not_take=func(index+1,prev)
            take=0
            if prev==-1 or pairs[index][0]>pairs[prev][1]:
                take= 1+func(index+1,index)
            ans=max(take,not_take)
            memo[(index,prev)]=ans
            return ans
        memo={}
        return func(0,-1)