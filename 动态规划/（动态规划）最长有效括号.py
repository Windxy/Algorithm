# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （动态规划）最长有效括号
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/30 14:34
**************************************************
'''
'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # dp设置和转移方程及解释如下：
        # dp[i]表示下标为i的数值对应最长长度
        # 当s[i]=="(":dp[i]为0
        # 当s[i]==")":
            # 当s[i-1]=="("：dp[i]==dp[i-2]+2
            # 当s[i-1]==")"且s[i - dp[i - 1] - 1]为"("：dp[i]==dp[i-1] + dp[i-dp[i-1]-2] + 2
        #注意:为什么是s[i - dp[i - 1] - 1]，这里例如((()()()),走到最后一个适合，dp[i-1]表示就是()()()的长度
        n = len(s)
        if n < 2:
            return 0
        dp = [0] * n
        dp[0] = 0
        if s[0]=='(' and s[1]==')':
            dp[1] = 2
        if n==2:
            return dp[1]

        for i in range(2,n):
            if s[i]=="(":
                dp[i]=0
            # if s[i]==")":
            #     if s[i-1]=="(":
            #         dp[i] = dp[i-2] + 2
            #     if i-dp[i-1]-1 >= 0 and s[i-1] == ")" and s[i-dp[i-1]-1] == "(":
            #         dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
            #     if s[i-1] == ")" and s[i-dp[i-1]-2] == "(":
            #         dp[i] = dp[i-1] + 2
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]

        return max(dp)

s = Solution()
s.longestValidParentheses("()(()))")