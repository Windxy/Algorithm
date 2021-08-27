# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （动态规划）通配符匹配
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/6 19:45
**************************************************
'''
'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
说明:
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:
输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:
输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wildcard-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)

        # 初始化
        dp = [[False]*(m+1) for _ in range(n+1)]

        dp[0][0] = True
        flag = 1
        for i in range(n):
            if p[i] == "*" and flag:
                dp[i+1][0] = True
            if p[i]!='*':
                flag=0

        # 如果p[i]=='?':
        # 如果p[i]=='*':
        # 如果p[i]=='字i母':
        for i in range(1,n+1):
            for j in range(1,m+1):
                if p[i-1]=="?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1] #匹配空或匹配多个
                else:
                    dp[i][j] = dp[i-1][j-1] and p[i-1]==s[j-1]
        return dp[n][m]

s="aab"
p="c*a*b"
a = Solution()
print(a.isMatch(s,p))