# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）括号生成
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/25 15:46
**************************************************
'''

'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 判断是否有效
        def valid(A):
            bal = 0
            for c in A:
                if c == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []

        def helper(s, path):
            nonlocal ans
            if not s:
                if valid(path):
                    ans.append(''.join(path))

            for i in range(len(s)):
                temp = s[i]
                if i>0 and s[i]==s[i-1]:continue
                del s[i]
                helper(s,path+[temp])
                s.insert(i,temp)

        s = ['('] * n + [')'] * n
        print(s)
        helper(s,[])
        return ans

s = Solution()
print(s.generateParenthesis(3))