# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）合并区间
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/19 21:31
**************************************************
'''
'''
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])#按照第一个元素进行排序
        ans = []
        for i in intervals:
            if len(ans)==0:
                ans.append(i)
            if ans[-1][1]>=i[0]:     # 如果最后一个元素的尾部大于了该元素的首部，说明重合，需要重新定义
                if ans[-1][1]>i[1]:
                    continue
                else:
                    ans[-1][1]=i[1]
            else:                   # 否则不重合
                ans.append(i)
        return ans
