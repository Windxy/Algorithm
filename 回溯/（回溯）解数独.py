# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 解数独
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/15 19:09
**************************************************
'''
from typing import List

# @xyz
class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def check(x, y, s):
            for i in range(9):
                if board[i][y] == s or board[x][i] == s:
                    return False
            for i in [0, 1, 2]:
                for j in [0, 1, 2]:
                    if board[x // 3 * 3 + i][y // 3 * 3 + j] == s:
                        return False
            return True

        def bt(cur):
            if cur == 81:
                return True
            x, y = cur // 9, cur % 9
            if board[x][y] != '.':
                return bt(cur + 1)
            for i in range(1, 10):
                s = str(i)
                if check(x, y, s):      #判断，在(x,y)位置，取s是否有效;否则，返回上一步
                    board[x][y] = s
                    if bt(cur + 1):     #判断下一步，如果有效，则说明可能是正确的，运气好的话，可能直接return True，但是某一步出错，就会换个i或者return False
                                        # 如果没有效果，则此步需要重新换数字，
                        return True
                    board[x][y] = '.'   #在（x,y位置），取s有效，但是下一步并不有效，所以这一步要重新来判断
            # （x,y）位置，取1-9都不行，那么说明是前面的步骤需要修改出现问题，返回上一层
            return False

        bt(0)

s = Solution()
b = [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
print(s.solveSudoku(b))