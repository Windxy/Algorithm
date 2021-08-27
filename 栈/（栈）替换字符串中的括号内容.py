'''
给你一个字符串 s ，它包含一些括号对，每个括号中包含一个 非空 的键。

比方说，字符串 "(name)is(age)yearsold" 中，有 两个 括号对，分别包含键 "name" 和 "age" 。
你知道许多键对应的值，这些关系由二维字符串数组 knowledge 表示，其中 knowledge[i] = [keyi, valuei] ，表示键 keyi 对应的值为 valuei 。

你需要替换 所有 的括号对。当你替换一个括号对，且它包含的键为 keyi 时，你需要：

将 keyi 和括号用对应的值 valuei 替换。
如果从 knowledge 中无法得知某个键对应的值，你需要将 keyi 和括号用问号 "?" 替换（不需要引号）。
knowledge 中每个键最多只会出现一次。s 中不会有嵌套的括号。

请你返回替换 所有 括号对后的结果字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/evaluate-the-bracket-pairs-of-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dict1 = {i[0]:i[1] for i in knowledge}

        index = 0
        ans = ""
        while index < len(s):
            if s[index] == '(':#如果遇到了左括号
                left = index+1
                while s[index]!=')':#遇到右括号之前
                    index+=1
                right = index
                if s[left:right] in dict1:
                    temp = dict1[s[left:right]]
                    # s[left:right] = temp # 不支持赋值
                    ans += temp
                else:
                    ans += "?"
            else:
                ans += s[index]
            index += 1
        print(ans)

s = Solution()
st = "(a)(a)(a)aaa"
knowledge = [["a","yes"]]
s.evaluate(st,knowledge)