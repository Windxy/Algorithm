''''''
'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。
'''
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''c，根号'''
        '''找到最小和最大'''
        right = int(math.sqrt(c))
        left = 0
        while left<=right:
            if left*left+right*right == c:
                return True
            if left*left+right*right < c:
                left += 1
            else:
                right -= 1
        print(False)
        return False
s = Solution()
s.judgeSquareSum(2)