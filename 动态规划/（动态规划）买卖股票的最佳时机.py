# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 买卖股票的最佳时机
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/8 15:24
**************************************************
'''
'''
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        min_price = prices[0]
        ans = 0
        dp = []
        for i in range(1,len(prices)):
            min_price = min(min_price,prices[i])    # 记录从1到i位置的最小值
            dp.append(0 if prices[i] - min_price < 0 else prices[i] - min_price)    # 这里可以直接转为普通变量，使得空间复杂度从n-->1
            ans = max(ans,dp[i-1])                  # 或dp，转移方程为dp[i] = max(dp[i-1],prices-minprices)
        return ans

    def maxProfit2(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            minprice = min(minprice, price)
            maxprofit = max(maxprofit, price - minprice)
        return maxprofit

    def maxProfit3(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        min_price = prices[0]
        ans = 0
        for i in range(1,len(prices)):
            min_price = min(min_price,prices[i])    # 记录从1到i位置的最小值
            ans = max(ans,0 if prices[i] - min_price < 0 else prices[i] - min_price)
        return ans
s = Solution
list =  [1,2,3,4]
print(s.maxProfit3(self=None,prices=list))