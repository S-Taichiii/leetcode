class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)): return False
        
        hash = {}
        for i in range(len(s)):
            if not s[i] in hash: hash[s[i]] = t[i]
            else:
                if hash[s[i]] != t[i]: return False

        return True


solution = Solution()
print( solution.isIsomorphic("foo", "baa") )
print( solution.isIsomorphic("paper", "title") )
print( solution.isIsomorphic("add", "bar") )
print( solution.isIsomorphic("abcd", "baba") )
#
# runtime 35ms 90.56%beats
# memory  16.73MB 34.61%beats
