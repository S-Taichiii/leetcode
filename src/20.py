class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        stack = []
        hash = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in hash and len(stack) != 0 and stack[len(stack) - 1] == hash[char]:
                stack.pop(len(stack) - 1)
                continue
            stack.append(char)

        return len(stack) == 0

solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("()"))
print(solution.isValid("(]"))
print(solution.isValid("{([])}"))

# 42ms
# Beats15.71%
# 16.53MB
# Beats40.65%
