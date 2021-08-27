from typing import List
'''https://leetcode-cn.com/problems/maximum-non-negative-product-in-a-matrix/'''
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        # 令dp_max[i][j]表示为从【0，0】到【i,j】位置最大的值；dp_min表示最小值
        # 边界：dp[0][0]=grid[0][0]，dp[i][0] = 连乘s[i][0]，dp[0][i] = 连乘s[0][i]
        # 状态转移方程：
        # dp_max[i][j] = max(grid[i][j]*(dp[i][j-1],dp[i-1][j]))
        # dp_min[i][j] = min(grid[i][j]*(dp[i][j-1],dp[i-1][j]))
        N = len(grid)
        N2 = len(grid[0])
        dp_min = [[0] * N2 for _ in range(N)]
        dp_max = [[0] * N2 for _ in range(N)]
        dp_max[0][0] = dp_min[0][0] = grid[0][0]
        # 边界处理
        for i in range(1, N):
            dp_max[i][0] = dp_max[i - 1][0] * grid[i][0]
            dp_min[i][0] = dp_min[i - 1][0] * grid[i][0]
        for i in range(1, N2):
            dp_max[0][i] = dp_max[0][i - 1] * grid[0][i]
            dp_min[0][i] = dp_min[0][i - 1] * grid[0][i]

        # 状态转移
        for i in range(1, N):  # 行
            for j in range(1, N2):  # 列
                dp_min[i][j] = min(
                    grid[i][j] * dp_max[i - 1][j], grid[i][j] * dp_max[i][j - 1],
                    grid[i][j] * dp_min[i - 1][j], grid[i][j] * dp_min[i][j - 1]
                )
                dp_max[i][j] = max(
                    grid[i][j] * dp_max[i - 1][j], grid[i][j] * dp_max[i][j - 1],
                    grid[i][j] * dp_min[i - 1][j], grid[i][j] * dp_min[i][j - 1]
                )

        return -1 if dp_max[N - 1][N2 - 1] < 0 else dp_max[N - 1][N2 - 1] % (10**9+7)

grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]
s = Solution()
s.maxProductPath(grid)