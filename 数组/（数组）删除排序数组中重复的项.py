# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）删除排序数组中重复的项
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/27 9:26
**************************************************
'''
'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
示例 1:
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index != len(nums):
            if index > 0 and nums[index] == nums[index-1]:
                nums.pop(index)
            else:
                index += 1
        print(nums)
        return len(nums)

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
