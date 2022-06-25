'''
假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。
例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。
请计算出粉刷完所有房子最少的花费成本。
来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/JEj789
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # dp[i][0~2]表示第i个房子用0~2色的..
        # dp[i][k] = dp[i-1][k_d] + costs[i][k_d] ,k!=k_d
        N = len(costs)
        dp = [[0] * 3 for _ in range(N)]
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]
        if N == 1:
            return min(dp[-1][0], dp[-1][1], dp[-1][2])

        for i in range(N):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][1], dp[i - 1][0]) + costs[i][2]

        return min(dp[-1][0], dp[-1][1], dp[-1][2])