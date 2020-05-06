import math

class Solution:
    def findComplement(self, num: int) -> int:
        temp = int(math.log2(num)) + 1

        for i in range(temp):
            num = (num ^ (1 << i))

        return num




finder = Solution()
print(finder.findComplement(4))