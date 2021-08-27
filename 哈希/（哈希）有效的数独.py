# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （哈希）有效的数独
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/3 17:25
**************************************************
'''
'''有图
https://leetcode-cn.com/problems/valid-sudoku/
'''
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 哈希判重
        def valid(tmp):
            nums = list(filter(lambda x:x!='.',tmp))
            return len(nums)==len(set(nums))

        for i in range(9):
            if not valid(board[i]):
                return False
        for i in range(9):
            tmp = [tmp_2[i] for tmp_2 in board]
            if not valid(tmp):
                return False
        for i in range(3):
            for j in range(3):
                tmp = [board[c][r] for c in range(i*3,i*3+3) for r in range(j*3,j*3+3)]
                if not valid(tmp):
                    return False
        return True
str1 = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s = Solution()
print(s.isValidSudoku(str1))
