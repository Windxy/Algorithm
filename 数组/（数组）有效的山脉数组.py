# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）有效的山脉数组
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/11/3 14:31
**************************************************
'''
'''
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        flag = 0
        for i in range(len(A)):
            if i>0 and flag == 0 and A[i]>A[i-1]:
                flag = 1
            if i>0 and flag == 0 and A[i]<A[i-1]:
                return False
            if i>0 and flag == 1 and A[i]<A[i-1]:
                flag = 2
            if i>0 and flag == 2 and A[i]>A[i-1]:
                return False
        if flag == 2:
            return True
        return False