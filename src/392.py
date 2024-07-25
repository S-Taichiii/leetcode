class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        match = []
        for char in s:
            if i >= len(t):
                return False
            while i < len(t):
                if char == t[i]:
                    i += 1
                    match.append(char)
                    break
                i += 1

        return len(s) == len(match)

# 42ms
# Beats17.41%
# 16.72MB
# Beats6.13%

class Solution:
    def solution(self, s: str, t: str) -> bool:
        sptr, tptr = 0, 0
        while sptr < len(s) and tptr< len(t):
            if s[sptr] == t[tptr]:
                sptr += 1
            tptr += 1

        if sptr == len(s): return True
        
        return False

# 38ms
# Beats42.90%
# 16.62MB
# Beats19.85%
            
solution = Solution()
print(solution.isSubsequence("acb", "ahbgc"))
print(solution.isSubsequence("abc", "ahbgc"))
print(solution.isSubsequence("axc", "ahbdgc"))
print(solution.isSubsequence("acx", "abcdef"))
print(solution.isSubsequence("aaaaaa", "bbaaa"))
print(solution.isSubsequence("ab", "baab"))
print(solution.isSubsequence("bb", "abcdef"))

