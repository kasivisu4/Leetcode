class Solution:
    def rob(self, nums: List[int]) -> int:
        # Using dp array
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         if len(nums)<=1:
#             return dp[-1]
#         dp[1] = max(nums[1],nums[0])
#         for i in range(2,len(nums)):
#             dp[i]=max(dp[i-2]+nums[i],dp[i-1])
#         return dp[-1]
        # Using 2 pointers
        prev_sum = nums[0]
        if len(nums)<=1:
            return prev_sum
        curr_sum = max(prev_sum,nums[1])
        for i in range(2,len(nums)):
            temp = curr_sum
            curr_sum = max(prev_sum+nums[i],curr_sum)
            prev_sum = temp
        return curr_sum