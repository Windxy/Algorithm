# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （字符串）比较含退格的字符串
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/19 21:16
**************************************************
'''
'''
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。
示例 1：
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：
输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s:str)->str:
            stack = []
            for i in s:
                if i!='#':
                    stack.append(i)
                else:
                    if stack:
                        stack.pop(-1)
            return stack

        return helper(S)==helper(T)

s = Solution()
print(s.backspaceCompare(S = "##a#c#", T = "b"))
