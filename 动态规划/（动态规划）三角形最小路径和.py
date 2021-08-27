''''''

'''
示例 1：
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

示例 2：
输入：triangle = [[-10]]
输出：-10

链接：https://leetcode-cn.com/problems/triangle
'''
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''动态规划'''
        '''
        自顶向下：
        dp[i][j] = min(dp[i-1][j],dp[i-1][j-1]) + triangle[i][j]   j != 0 or i
        dp[i][j] = dp[i-1][0]   + triangle[i][j]  j == 0
        dp[i][j] = dp[i-1][i-1] + triangle[i][j]  j == i
        '''

        lens = len(triangle)
        dp = [[0]*lens for _ in range(lens)]
        dp[0][0] = triangle[0][0]

        '''自顶向下'''
        for i in range(1,lens):     #假设有5层，那么i是1到4
            for j in range(i+1):    #j是0到i
                if j == 0:
                    dp[i][j] = dp[i-1][0] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][i-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
        ans = dp[lens-1][0]
        for num in dp[lens-1]:
            ans = min(ans,num)
        print(ans)

        road = []
        # 根据dp获取得到路径 O(n^2)
        for i in range(lens-1,-1,-1):   #4->0
            temp = 0
            flag = dp[i][temp]
            for j in range(len(triangle[i])):
                if flag > dp[i][j]: #找到最小
                    flag = dp[i][j]
                    temp = j
            road.append(temp)
        print(road)
        return ans



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
s = Solution()
s.minimumTotal(triangle)