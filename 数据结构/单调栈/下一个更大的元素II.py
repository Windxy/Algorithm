'''
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈+重构数组
        stack = []
        ans = [-1]*len(nums)

        for i in range(2*len(nums)-1,-1,-1):
            cur_idx = i%len(nums)
            while stack and stack[-1] <= nums[cur_idx]: # 有重复的
                stack.pop()
            if not stack:
                ans[cur_idx] = -1
            else:
                ans[cur_idx] = stack[-1]
            stack.append(nums[cur_idx])
        #     print(ans[cur_idx],stack)
        # print(ans)
        return ans