# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （栈）
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/23 14:05
**************************************************
'''
'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def isValid(s: str) -> bool:
    # 栈
    # 或者用字符表达
    dic = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for i in s:
        if i in dic.keys() and len(stack)!=0: # 如果i在字典中，同时stack不为空
            if stack[-1]==dic[i]:stack.pop()
            else:return False
            continue
        stack.append(i)

    return False if len(stack)!=0 else True

print(isValid(s = "()"))