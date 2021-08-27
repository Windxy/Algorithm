# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （二分）在排序数组中查找元素的第一个和最后一个位置
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/3 16:24
**************************************************
'''
'''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 按照正常二分查找的规则，是不一定找得到边界的，因此不能对设置if条件（相等判断）跳出
        # 要找到最左，就要让right一直靠近left，设置nums[mid]>=target则right=mid
        if len(nums)==0:return [-1,-1]
        left = 0
        right = len(nums) - 1
        while left<right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        # return left
        if nums[left] != target:
            return [-1,-1]
        tmp = left
        while True:
            if tmp == len(nums) or nums[tmp] > nums[left]:
                break
            tmp += 1
        return [left,tmp-1]
nums = [5,7,7,8,8,10]
target = 7
s = Solution()
print(s.searchRange(nums,target))