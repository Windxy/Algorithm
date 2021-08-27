# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （贪心）跳跃游戏2
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/7 20:23
**************************************************
'''
'''
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step

    def jump2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        times = 0   #总计跳跃次数
        max_now = 0 #当前步下能到达的最大位置，比如【2，3，4，1】在第一步，可到达的位置是下标3
        ind = 0     #当前下标位置
        max_step = 0#最大能前行位置

        while max_now<len(nums)-1:  #说明还没到
            while ind<=max_now:     #从当前下标位置道能到达的最大位置，一步步找最大的能去的地方
                ind+=1
                max_step = max(max_step,ind+nums[ind])
            times += 1

        return times

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/jump-game-ii/solution/tiao-yue-you-xi-ii-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 官方复杂度O（n）
    def jump3(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:        # 如果到达了边界位置
                    step += 1       # 走一步
                    end = maxPos    # 然后更新最远长度
        return step