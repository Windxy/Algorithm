# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （字符串）最长公共前缀E
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/17 14:18
**************************************************
'''
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #匹配两个字符串的最长前缀
        def lcp(s1,s2):
            i,j=0,0
            while i<len(s1) and j<len(s2):
                if s1[i] == s2[j]:
                    i+=1
                    j+=1
                else:
                    break
            return s1[0:i]

        # 横向对比查找
        if strs==[]:return
        ans = strs[0]
        for i in range(1,len(strs)):
            ans = lcp(ans,strs[i])
        return ans


s = Solution()
l = []
s.longestCommonPrefix(l)