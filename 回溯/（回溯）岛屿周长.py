# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）岛屿周长
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/30 9:04
**************************************************
'''
'''
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例 :
输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
输出: 16
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/island-perimeter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dx = [0,0,-1,1]#上下左右
        dy = [-1,1,0,0]
        ans = 0
        def helper(x,y):
            nonlocal ans
            # 深度优先遍历
            if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==0:      #如果为水域，则加一个边
                return 1
            if x<0 or y<0 or x==len(grid) or y==len(grid[0]):                           #如果出界了，则加一个边
                return 1
            if grid[x][y]==2:   # 已经访问过了的话
                return 0

            grid[x][y] = 2      #开始访问这个
            return helper(x+dx[0],y+dy[0])+helper(x+dx[1],y+dy[1])+helper(x+dx[2],y+dy[2])+helper(x+dx[3],y+dy[3])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return helper(i,j)
        return ans

s = Solution()
print(s.islandPerimeter([[1,0]]))