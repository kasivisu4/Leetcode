class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currPosition = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i+nums[i] >= currPosition:
                currPosition = i
        return currPosition ==0 