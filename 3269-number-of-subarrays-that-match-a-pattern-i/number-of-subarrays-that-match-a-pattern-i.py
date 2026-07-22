class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        low=0
        high=0
        n=len(nums)
        k=len(pattern)+1
        cnt=0
        while high<n:
            if (high-low+1)<k:
                high+=1
            else:
                high+=1
                j=0
                check=True
                for i in range(low+1,high):
                    if pattern[j]==1 and nums[i-1]>=nums[i]:
                        check=False
                        break
                    elif pattern[j]==0 and (nums[i-1]<nums[i] or nums[i-1]>nums[i]):
                        check=False
                        break
                    elif pattern[j]==-1 and nums[i-1]<=nums[i]:
                        check=False
                        break
                    j+=1
                if check:
                    cnt+=1
                low+=1
        return cnt


                    


                
