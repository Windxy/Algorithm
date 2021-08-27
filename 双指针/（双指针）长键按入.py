# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （双指针）长键按入
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/21 8:50
**************************************************
'''
'''
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。
示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true
示例 4：
输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/long-pressed-name
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        t = 0
        flag = 1
        for i in range(len(typed)):
            if typed[i]==name[t]:
                t+=1
            else:   # 没有相等
                if i>0 and typed[i]==typed[i-1]:        # 如果上一次遍历了，而且是相同的
                    continue
                else:
                    return False
            if t==len(name):
                while i<len(typed)-1:
                    if typed[i]!=typed[i+1]:
                        return False
                    i+=1
                return True
        return False
s = Solution()
print(s.isLongPressedName(name = "alex", typed = "alexxr"))