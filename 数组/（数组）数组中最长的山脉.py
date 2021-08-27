# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）数组中最长的山脉
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/26 20:03
**************************************************
'''
'''
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
B.length >= 3
存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）
给出一个整数数组 A，返回最长 “山脉” 的长度。
如果不含有 “山脉” 则返回 0。
示例 1：
输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
示例 2：
输入：[2,2,2]
输出：0
解释：不含 “山脉”。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-mountain-in-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0

        n = len(A)
        left = [0] * n
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if A[i - 1] < A[i] else 0)

        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if A[i + 1] < A[i] else 0)

        ans = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)

        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/longest-mountain-in-array/solution/shu-zu-zhong-de-zui-chang-shan-mai-by-leetcode-sol/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。