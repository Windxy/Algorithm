'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 分治迭代
        def getKth(k, idx1, idx2):
            if idx1 == n:               # 如果idx1到尽头了，说明答案在nums2处
                return nums2[idx2+k-1]  # nums下标为idx2+k-1处
            if idx2 == m:               # 同理
                return nums1[idx1+k-1]
            if k == 1:
                return min(nums1[idx1], nums2[idx2])

            new_idx1 = min(idx1 + k // 2 - 1 , n-1)
            new_idx2 = min(idx2 + k // 2 - 1 , m-1)
            num1, num2 = nums1[new_idx1], nums2[new_idx2]
            if num1 <= num2:                    # 说明num1前面的都要抛弃，这里等于去掉也没关系
                k = k - (new_idx1 - idx1 + 1)   # 此时，下标k更新为抛弃了num1前面数值的序号
                idx1 = new_idx1 + 1             # 同时，idx1+1，因为前面的都没有用了，以及，k向前移动了
            else:
                k = k - (new_idx2 - idx2 + 1)   # 同理
                idx2 = new_idx2 + 1
            return getKth(k, idx1, idx2)

        n, m = len(nums1), len(nums2)
        m_n = m + n
        if (m + n) % 2 == 1:
            return getKth((m_n + 1) // 2, 0, 0)
        else:
            return (getKth(m_n // 2, 0, 0) + getKth((m_n) // 2 + 1, 0, 0)) / 2