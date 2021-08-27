# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）n皇后2
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/16 9:18
**************************************************
'''
# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）n皇后
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/15 14:25
**************************************************
'''
'''
给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def check(self,maze,row,col):
        # 判断是否可以构成可行集
        if row==0:
            return 1

        temp = 1  # 设为1是因为最少要从上一行开始检查
        while temp <= row:  # 因为是从上往下，逐行下子，所以只需要考虑这一行是否和上面的相互冲突就行。
            if maze[row - temp][col] == "Q":  # 同列检查
                return 0
            if (col - temp >= 0) and (maze[row - temp][col - temp] == "Q"):  # 左上斜方向检查
                return 0
            if (col + temp < len(maze)) and (maze[row - temp][col + temp] == "Q"):  # 右上斜方向检查
                return 0
            temp += 1  # 如果当前行比较深，就再检查上上一行是否冲突
        return 1


    def totalNQueens(self, n: int) -> List[List[str]]:
        # 1.初始化
        maze = [['.' for i in range(n)] for i in range(n)]
        ans = 0

        def helper(maze, size, row):
            nonlocal ans
            if row == size:
                ans += 1
                return

            for i in range(size):
                maze[row][i] = 'Q'  # 试探下
                if self.check(maze, row, i):
                    helper(maze,size, row + 1)
                maze[row][i] = '.'  # 恢复下

            return

        helper(maze,n,0)
        # print(ans)
        return ans

s = Solution()
s.totalNQueens(4)