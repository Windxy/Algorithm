'''
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # hash  + 单调栈
        dic = {}
        d_stack = []
        for idx in range(len(nums2)-1,-1,-1):
            while d_stack and d_stack[-1] < nums2[idx]:
                d_stack.pop()
            if not d_stack: # 如果到达栈底
                dic[nums2[idx]] = -1
            else:
                dic[nums2[idx]] = d_stack[-1]
            d_stack.append(nums2[idx])

        ans = [dic[n] for n in nums1]
        return ans