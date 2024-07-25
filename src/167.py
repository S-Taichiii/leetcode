from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lptr = 0
        rptr = len(numbers) - 1

        while lptr < rptr:
            total = numbers[lptr] + numbers[rptr]
            if total == target:
                return [lptr + 1, rptr + 1]

            if total <= target:
                lptr += 1
            else:
                rptr -= 1
            
        return []
            

# 104ms
# Beats61.71%
# 17.74MB
# Beats15.66%

solution = Solution()
print(solution.twoSum([2, 4, 5, 6,7, 8, 9], 9))
print(solution.twoSum([2, 3, 4], 6))
print(solution.twoSum([-1, 0], -1))
print(solution.twoSum([-1000,-1,0,1],1))
