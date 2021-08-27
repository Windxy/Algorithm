# coding:utf-8
'''
**************************************************
@File   ：python_dp -> Z字形变换（list）
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/13 21:45
**************************************************
'''
'''将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
def convert( s: str, numRows: int) -> str:
    if numRows < 2: return s
    res = ["" for _ in range(numRows)]
    i, flag = 0, -1
    for c in s:
        res[i] += c
        if i == 0 or i == numRows - 1: flag = -flag
        i += flag
    return "".join(res)


convert('ABCCC',2)
# LCIRETOESIIGEDHN
# LCIRETOESIIGEDHN