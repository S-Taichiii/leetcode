from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in hash: hash[num] = i
            else:
                if abs(hash[num] - i) <= k: return True
                else: hash[num] = i

        return False
        
solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))
print(solution.containsNearbyDuplicate([1, 0, 1, 1], 1))
print(solution.containsNearbyDuplicate([1, 2, 3, 1], 3))

# 470ms
# Beats30.42%
# 29.89MB
# Beats32.66%
