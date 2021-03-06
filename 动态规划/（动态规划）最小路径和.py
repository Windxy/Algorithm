# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （动态规划）最小路径和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/28 15:43
**************************************************
'''
'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        m,n = len(grid),len(grid[0])
        dp = [[0 for i in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]

        for i in range(1,n):
            dp[0][i] = dp[0][i-1]+grid[0][i]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        # print(dp[m-1][n-1])
        return dp[m-1][n-1]
lists = [[0,1],[1,0]]
s = Solution()
s.minPathSum(lists)