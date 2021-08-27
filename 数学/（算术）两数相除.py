# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （算术）两数相除
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/29 18:40
**************************************************
'''
'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        flag = 1
        if dividend ^ divisor < 0: flag = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                result += i
                i <<= 1
                tmp <<= 1
        result = result * flag
        return min(max(-2 ** 31, result), 2 ** 31 - 1)


# 作者：zkk-c
# 链接：https://leetcode-cn.com/problems/divide-two-integers/solution/bao-li-jia-you-hua-by-zkk-c/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。