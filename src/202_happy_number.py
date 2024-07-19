# blutal force
class Solution:
    def isHappy(self, n: int) -> bool:
        known = set()
        while n != 1:
            n = sum([int(num) ** 2 for num in str(n)])
            if n in known: return False

            known.add(n)

        return True
        

solution = Solution()
print(solution.isHappy(19))
print(solution.isHappy(2))
print(solution.isHappy(7))

# 34ms 76,56%
# 16.35MB 90.41%


# フロイドの循環検出アルゴリズム
class Froid:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)

        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

        return fast == 1

    def get_next(self, n: int) -> int:
        return sum([int(num) ** 2 for num in str(n)])

froid = Froid()
print(froid.isHappy(19))

# 30ms 91.81%
# 16.37MB 90.41%
