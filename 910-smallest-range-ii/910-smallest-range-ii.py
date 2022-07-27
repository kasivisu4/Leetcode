class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = nums[-1]-nums[0]
        temp_min = nums[0]
        temp_max = nums[-1]
        for i in range(1,len(nums)):
            temp_min = min(nums[0]+k,nums[i]-k)
            temp_max = max(nums[-1]-k,nums[i-1]+k)
            ans=min(ans,temp_max-temp_min)
        return ans