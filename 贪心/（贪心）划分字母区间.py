# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （贪心）划分字母区间
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/23 9:02
**************************************************
'''
'''
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-labels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dict = {}
        for i in range(len(S)):
            dict[S[i]] = i      # 记录每个字母最后出现的下标
        start,end = 0,0         # 双指针
        endc = dict[S[0]]          # 记录边界
        ans = []
        while start < len(S): # 没有达到终止条件时候
            while end < endc:
                endc = max(endc,dict[S[end]])  #更新endc
                end += 1 # 追赶endc
            if end!=len(S)-1:
                end = end+1
                endc = dict[S[end]]
                ans.append(len(S[start:end]))
                start = end
            else:
                ans.append(len(S[start:len(S)]))
                start = len(S)
        print(ans)
        return ans
s = Solution()
s.partitionLabels('ababcbacadefegdehijhklij')