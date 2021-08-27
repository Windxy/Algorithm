# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）缺失的第一个正数
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/4 15:28
**************************************************
'''
'''
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
示例 1:
输入: [1,2,0]
输出: 3
示例 2:
输入: [3,4,-1,1]
输出: 2
示例 3:
输入: [7,8,9,11,12]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 1
        i = 1
        while True:     #暴力法
            if i not in nums:
                return i
            i += 1