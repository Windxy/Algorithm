# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 【数组】较大分组的位置
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2021/1/5 15:38
**************************************************
'''
# 在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
# 例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
# 分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。
# 我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
# 找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。
# 示例 1：
# 输入：s = "abbxxxxzzy"
# 输出：[[3,6]]
# 解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/positions-of-large-groups
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        '''直接模拟解答'''
        ans = []
        nums = 0
        if len(s)<3:
            return []
        i = 1
        start = 0
        while i<len(s):
            if s[i]==s[i-1]:
                nums += 1
                start = i-1
                while i < len(s) and s[i]==s[i-1]:
                    nums+=1
                    i+=1
                if nums>=3:
                    ans.append([start, i-1])
            nums=0
            i+=1
        print(ans)
        return ans
s = Solution()
s.largeGroupPositions(s='abcdddeeeeaabbbcd')