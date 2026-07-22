class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pos=0
        neg=1
        result=[0]*n
        for num in nums:
            if num<0:
                result[neg]=num
                neg+=2
            else:
                result[pos]=num
                pos+=2
        return result