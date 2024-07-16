class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordList = s.split(" ")

        if len(set( pattern )) != len(set( wordList )) or len(pattern) != len(wordList): return False

        hash = {}
        for i in range(len(pattern)):
            word = wordList[i]
            if pattern[i] not in hash: hash[pattern[i]] = word
            else: 
                if hash[pattern[i]] != word:
                    return False

        return True


solution = Solution()
print(solution.wordPattern("abba", "dog cat cat fish"))
print(solution.wordPattern("abba", "dog cat cat dog"))
print(solution.wordPattern("aaaa", "dog cat cat fish"))
        
# 36ms 48.01%
# 16.54MB 29.51%
