# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （双指针）有序数组的平方
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/16 9:03
**************************************************
'''
'''
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n

        i, j = 0, n-1
        index = n-1
        while i <= j:
            if A[i]*A[i]<=A[j]*A[j]:
                ans[index] = A[j]*A[j]
                j-=1
            else:
                ans[index] = A[i]*A[i]
                i+=1
            index -= 1

        # print(ans)
        return ans

s = Solution()
s.sortedSquares([-4,-1,0,3,10])