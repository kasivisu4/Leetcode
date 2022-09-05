class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        minNumber = float("inf")
        if not 1 in nums:
            return 1
        for i in nums:
            if i+1 not in nums and i>0:
                if minNumber>i+1:
                    minNumber = i+1
        return minNumber
        
        