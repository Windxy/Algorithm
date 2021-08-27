# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 最长回文子串
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/12 21:39
**************************************************
'''
'''给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def longestPalindrome(self, s):
        if s==None:return ""
        if len(s)==1:return s
        if len(s)==2:return s if s[0]==s[1] else s[0]
        ans = ""
        lens = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(len(s)):
            dp[i][i] = True
            if i<len(s)-1:
                dp[i][i+1] = (s[i]==s[i+1])
        for j in range(1, len(s)):
            for i in range(0, j):
                if i+1!=j:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
        for i in range(len(s)):
            for j in range(len(s)):
                if dp[i][j] and j-i>=lens:
                    ans = s[i:j+1]
                    lens = j-i
        print(ans)
        return ans
str = 'cbbd'
s = Solution()
s.longestPalindrome(str)