# https://leetcode-cn.com/problems/delete-and-earn/

'''
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-and-earn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

'''
from typing import  List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''跟打家劫舍一个道理'''
        max_nums = 0
        for i in nums:
            max_nums = max_nums if i < max_nums else i
        new_nums = [0]*(max_nums+1)
        for i in nums:
            new_nums[i-1] += 1

        for i in range(len(new_nums)):
            new_nums[i] = new_nums[i]*(i+1)

        '''dp[i] = max(dp[i-1],dp[i-2]+new_nums[i])，当前位置下的最大的值等于
        删除该值 或 删除前面的值再加上当前的值'''

        dp = [0]*len(new_nums)
        dp[0] = new_nums[0]
        for i in range(1,len(new_nums)):
            dp[i] = max(dp[i-1],dp[i-2]+new_nums[i])    #状态转移方程
        print(dp[-1])
        return dp[-1]

nums = [1]
s = Solution()
s.deleteAndEarn(nums)