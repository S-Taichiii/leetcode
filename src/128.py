from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)

        sorted_list = sorted(nums)
        used = set()
        max = 1
        count = 1

        for i in range(1, len(sorted_list)):
            if sorted_list[i] in used: continue
            if sorted_list[i] - sorted_list[i - 1] == 1:
                count += 1
                if count > max: max = count
            else: count = 1

            used.add(sorted_list[i])

        return max

solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2]))
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(solution.longestConsecutive([1, 2, 0, 1]))


# 356ms
# Beats59.63%
# 32.21MB
# Beats16.48%


