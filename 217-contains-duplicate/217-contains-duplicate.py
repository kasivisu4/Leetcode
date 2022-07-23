class Solution:
    # Approach 1 : O(n^2)
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if nums[i]==nums[j]:
    #                 return True
    #     return False
    # Approach 2 : O(n log n)
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums.sort()
#         for i in range(0,len(nums)-1):
#             if(nums[i]==nums[i+1]):
#                 return True
#         return False
     # Approach 3 : O(n) Hash Set
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for num in nums:
            if num in temp:
                return True
            else:
                temp.add(num)
        return False
    
    
        
    