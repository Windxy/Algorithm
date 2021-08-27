# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数学）x的平方根
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/11/4 16:22
**************************************************
'''

class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r*r > x:
            r = (r+x/r)//2 #大于等于根号x，不等式
        return int(r)