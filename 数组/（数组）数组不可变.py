# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 数组不可变
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/9 13:45
**************************************************
'''
'''给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。'''
'''https://leetcode-cn.com/problems/range-sum-query-immutable/'''
from typing import List
class NumArray:
    def __init__(self, nums: List[int]):
        self.num = [0]*len(nums)
        if len(nums)==0:return
        self.num[0] = nums[0]
        for i in range(1,len(nums)):
            self.num[i] = nums[i]+self.num[i-1]    #'''求i到j就是0到j的和减去0到i的和'''

    def sumRange(self, i: int, j: int) -> int:
        if len(self.num) == 0: return
        if i==0:return self.num[j]
        return self.num[j]-self.num[i-1]


# Your NumArray object will be instantiated and called as such:
nums = []
obj = NumArray(nums)
param_1 = obj.sumRange(1,2)
print(param_1)