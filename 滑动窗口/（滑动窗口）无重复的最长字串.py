# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 无重复的最长子串
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/11 14:41
**************************************************
'''
'''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。'''
'''输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''
'''https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 一次遍历
        if len(s)==1 or len(s) == 0:return len(s)

        tmp = {}        # 用于判断是否有重复项，以及最大的长度
        this = []
        for i,j in enumerate(s):        # j为此字符
            if j in tmp.keys():         # 如果有此数的话，将答案进行更改
                # ans = max(ans,i-tmp[j])
                this.append(i+1-tmp[j] if this[i-1]+1 >= i+1-tmp[j] else this[i-1]+1)
                tmp[j] = i+1
            else:
                tmp[j] = i+1
                if i!=0:
                    this.append(this[i-1]+1)
                else:
                    this.append(1)#第一个
            # tmp[j] = i
        return max(this)

s= Solution()
print(s.lengthOfLongestSubstring("ab"))