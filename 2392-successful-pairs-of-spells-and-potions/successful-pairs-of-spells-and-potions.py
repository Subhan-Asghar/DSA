class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result=[]
        n=len(potions)
        potions.sort()
        for num in spells:
            low=0
            high=n-1
            while low<high:
                mid=(low+high)//2
                val=num*potions[mid]
                if val>=success:
                    high=mid
                else:
                    low=mid+1
            if num*potions[high]>=success:
                result.append(n-high)
            else:
                result.append(0)
        return result