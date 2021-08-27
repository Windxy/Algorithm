# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）颜色分类
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/7 20:27
**************************************************
'''
'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a,b,c = 0,0,0
        for i in nums:
            if i==0:a+=1
            if i==1:b+=1
            if i==2:c+=1
        index = 0
        tmp1,tmp2,tmp3 = 0,0,0
        while tmp1<a:
            nums[index]=0
            index += 1
            tmp1 += 1

        while tmp2<b:
            nums[index]=1
            index += 1
            tmp2 += 1

        while tmp3<c:
            nums[index]=2
            index += 1
            tmp3 += 1