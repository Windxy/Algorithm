# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （数组）插入区间
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/19 21:48
**************************************************
'''
'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1：
输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：
输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def merge(intervals: List[List[int]]) -> List[List[int]]:
            intervals.sort(key=lambda x: x[0])  # 按照第一个元素进行排序
            ans = []
            for i in intervals:
                if len(ans) == 0:
                    ans.append(i)
                if ans[-1][1] >= i[0]:  # 如果最后一个元素的尾部大于了该元素的首部，说明重合，需要重新定义
                    if ans[-1][1] > i[1]:
                        continue
                    else:
                        ans[-1][1] = i[1]
                else:  # 否则不重合
                    ans.append(i)
            return ans
        # if len(intervals)<2 or newInterval[0]==newInterval[1]:
        #     intervals.append(newInterval)
        #     return merge(intervals)
        # for i in range(len(intervals)-1):
        #     if intervals[i][1]<newInterval[0] and intervals[i+1][0]>newInterval[1]:
        #         return intervals
        #     if intervals[i][0]<=newInterval[0] and intervals[i][1]>=newInterval[1]:
        #         return intervals
        # if intervals[-1][0] <= newInterval[0] and intervals[-1][1] >= newInterval[1]:
        #     return intervals
        intervals.append(newInterval)

        return merge(intervals)
s = Solution()
print(s.insert([[3,5],[12,15]],[6,6]))