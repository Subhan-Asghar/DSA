from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        low=0
        hashmap=defaultdict(int)
        seen=set()
        max_value=0
        for high in range(len(fruits)):
            while fruits[high] not in seen and len(seen)==2:
                hashmap[fruits[low]]-=1
                if hashmap[fruits[low]]==0:
                    seen.remove(fruits[low])
                low+=1
            hashmap[fruits[high]]+=1
            seen.add(fruits[high])
            max_value=max(max_value,high-low+1)
        return max_value
