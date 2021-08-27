# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 打家劫舍
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/8 15:41
**************************************************
'''
'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
考虑3种情况，
情况1，如果房屋只有1个，则直接返回这个房屋
情况2，如果房屋有两个，则返回最大的那个
情况3，如果房屋有2个以上，则dp[i] = max{dp[i-2]+a[i],dp[i-1]}，边界条件为，dp[0]=a[0],dp[1] = max(a[0],a[1])
'''
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1],nums[0])

        dp = [];dp.append(nums[0]);dp.append(max(nums[1],nums[0]))
        for i in range(2,len(nums)):
            dp.append(max(dp[i-2]+nums[i],dp[i-1]))

        return dp[len(nums)-1]
''' 
dp = [0]*len(nums)
if not nums <==> len(nums)==0
'''
s = Solution
list = [2,7,9,3,1]
print(s.rob(self=None,nums=list))