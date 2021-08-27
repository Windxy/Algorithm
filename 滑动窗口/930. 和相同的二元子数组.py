'''
给你一个二元数组 nums ，和一个整数 goal ，请你统计并返回有多少个和为 goal 的 非空 子数组。
子数组 是数组的一段连续部分。

示例 1：
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-subarrays-with-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # 滑动窗口
        left,right = 0,0
        All_nums = nums[0]
        count = 0
        while right < len(nums):
            # 如果大了，left右移
            # 如果小了，right右移
            if All_nums < goal and right+1<len(nums):
                right += 1
                All_nums += nums[right]
            elif All_nums > goal:
                All_nums -= nums[left]
                left += 1
            else:
                if All_nums==goal:
                    count += 1
                if right+1<len(nums) and nums[right+1]==0:
                    right += 1
                    All_nums += nums[right]
                elif left<len(nums):
                    All_nums -= nums[left]
                    left += 1
                else:
                    return count
        # print(count)
        return count


s = Solution()
print(s.numSubarraysWithSum([0,0,0,0,0],0))