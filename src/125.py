class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        list = []

        for char in s:
            if ord('a') <= ord(char) and ord(char) <= ord('z') or char.isdecimal():
                list.append(char)
                

        left = 0
        right = len(list) - 1
        while left < right:
            if list[left] != list[right]: return False
            left += 1
            right -= 1

        return True 

# 56ms
# Beats13.34%
# 17.72MB
# Beats30.92%

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))
print(solution.isPalindrome(" "))
print(solution.isPalindrome("a a"))
print(solution.isPalindrome("       "))
print(solution.isPalindrome("0P"))

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^A-Za-z0-9]", "", s).lower()
        return s == s[::-1]

# 42ms
# Beats72.92%
# 18.08MB
# Beats20.69%
