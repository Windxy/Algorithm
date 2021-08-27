# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 寻找两个正序数组的中位数
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/12 21:15
**************************************************
'''
'''
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
你可以假设 nums1 和 nums2 不会同时为空。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = nums1+nums2
        ans.sort()
        return ans[len(ans)//2] if len(ans)%2!=0 else (ans[len(ans)//2]+ans[len(ans)//2-1])/2

a = [1,3]
b = [2,4]
s = Solution
print(s.findMedianSortedArrays(None,a,b))