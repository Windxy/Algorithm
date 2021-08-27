# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 最大子序列和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/8 14:26
**************************************************
'''
'''https://leetcode-cn.com/problems/maximum-subarray/'''
'''给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。'''
'''解析：如果要求得第i个位置的最大和dp[i]，就要知道前一个最大和dp[i-1]与自身相加是否比自身大，是，则dp[i]=dp[i-1]+a[i]，否则a[i]'''
'''状态转移方程为dp[i] = max{ dp[i-1]+a[i] . a[i] }'''
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = []
        ans = nums[0]
        dp.append(nums[0])
        for i in range(1,n):
            dp.append(max(dp[i-1]+nums[i], nums[i]))        # dp.append(dp[i-1]+nums[i] if dp[i-1]>0 else nums[i])
            ans = max(dp[i],ans)
        return ans

s = Solution
list =  [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(self=None,nums=list))