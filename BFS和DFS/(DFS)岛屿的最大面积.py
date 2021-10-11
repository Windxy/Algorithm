'''https://leetcode-cn.com/problems/max-area-of-island/'''
'''
给你一个大小为 m x n 的二进制矩阵 grid 。
岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
岛屿的面积是岛上值为 1 的单元格的数目。
计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。
'''
from  typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        Rows = len(grid)
        Cols = len(grid[0])
        ans = 0
        turnLRTD = [[-1,0],[1,0],[0,1],[0,-1]]
        max_temp = 0

        def helper(x,y):
            nonlocal max_temp
            if grid[x][y] == 1:
                max_temp += 1
                grid[x][y] = 0
                for a,b in turnLRTD:
                    if x+a < Rows \
                    and x+a >= 0 \
                    and y+b < Cols \
                    and y+b >= 0 \
                    and grid[x+a][y+b]==1:  # 提前剪枝
                        helper(x+a,y+b)

        for i in range(Rows):
            for j in range(Cols):
                if grid[i][j] == 1:
                    helper(i,j)
                    ans = max(ans,max_temp)
                    max_temp = 0

        return ans