# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （字符串）字符串相乘
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/5 9:15
**************************************************
'''
'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        res = [0] * (len(num1) + len(num2))
        for index1, i in enumerate(num1[::-1]):
            for index2, j in enumerate(num2[::-1]):
                tmp = res[index1 + index2] + int(i) * int(j)    #官方的第二种解法
                res[index1 + index2] = tmp % 10
                res[index1 + index2 + 1] += tmp // 10

        result = ''

        for i in res[::-1]:
            result += str(i)

        return result.lstrip('0')


# 作者：cccober - 2
# 链接：https: // leetcode - cn.com / problems / multiply - strings / solution / yi - chong - yi - li - jie - de - jian - duan - pythonshi - xian - by - /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。