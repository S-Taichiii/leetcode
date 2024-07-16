import unittest

def canConstruct(ransomNote: str, magazine: str) -> bool:
    hash = {}
    for c in magazine:
        if c in hash.keys(): hash[c] += 1
        else: hash[c] = 1

    for c in ransomNote:
        if c in hash.keys() and hash[c] > 0: hash[c] -= 1
        else: return False

    return True


class Test(unittest.TestCase):
    def test1(self):
        value = canConstruct("aa", "aac")
        self.assertTrue(value)

    def test2(self):
        value = canConstruct("a", "b")
        self.assertFalse(value)

    def test3(self):
        value = canConstruct("aa", "ab")
        self.assertFalse(value)

    def test4(self):
        value = canConstruct("aab", "baa")
        self.assertTrue(value)

if __name__ == "__main__":
        
    unittest.main()

