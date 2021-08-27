# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （动态规划）不同路径2
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/27 15:55
**************************************************
'''
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]] ) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(n):
            if obstacleGrid[0][i]==1:
                break
            dp[0][i] = 1
        for i in range(m):
            if obstacleGrid[i][0]==1:
                break
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m-1][n-1]

