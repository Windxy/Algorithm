# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （字符串）二进制求和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/30 9:34
**************************************************
'''
'''
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
示例1:
输入: a = "11", b = "1"
输出: "100"
示例2:
输入: a = "1010", b = "1011"
输出: "10101"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/add-binary/solution/er-jin-zhi-qiu-he-by-leetcode-solution/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
