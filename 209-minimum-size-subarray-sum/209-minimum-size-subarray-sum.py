class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count = float("inf")
        left = 0
        sum = 0
        for i in range(0,len(nums)):
            sum+=nums[i]
            while(sum>=target):
                count = min(count,i-left+1)
                sum-=nums[left]
                left+=1
        if count==float("inf"):
            return 0
        return count
        
        