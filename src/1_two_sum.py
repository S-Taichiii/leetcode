from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in hash: return [hash[nums[i]], i]
            
            hash[diff] = i 

        return []

        
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([3, 3,], 6))

# 61ms 57.46%
# 17.96MB 7.19%
