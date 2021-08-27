# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）下一个排列
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/30 14:05
**************************************************
'''
'''
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1.从右向左找到第一个下降值
        flag_decent = len(nums)-1
        while flag_decent > 0:
            if nums[flag_decent] <= nums[flag_decent-1]:
                flag_decent -= 1
            else:
                break
        if flag_decent == 0:
            nums = nums.sort()
            return nums
        # 2.找出另一个最大索引 k 满足 nums[k] > nums[flag_decent-1]
        k = len(nums) - 1
        while k > flag_decent - 1:   #index  0
            if nums[k] > nums[flag_decent-1]:
                break
            k -= 1
        # 3.flag_decent-1后面的全部进行排序
        tmp = nums[k]
        nums[k] = nums[flag_decent-1]
        nums[flag_decent-1] = tmp
        nums[flag_decent:]=sorted(nums[flag_decent:])


# 1,2,3 → 1,3,2
s = Solution()
s.nextPermutation([3,2,1])