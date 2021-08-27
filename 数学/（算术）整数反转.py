# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 整数反转（算术）
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/13 19:54
**************************************************
'''
'''给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
输入: 123
输出: 321
示例 2:
输入: -123
输出: -321

120-->21
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

def reverse(x):
    flag = -1 if x<0 else 1
    an = abs(x)
    l = []      # 尝试去掉这个
    res = 0
    while(an>=10):
        l.append(an%10)
        an = an//10
    l.append(an%10)
    b = 1
    for i in range(len(l)):
         index = -1-i
         res += l[index]*b
         b*=10
    print(res*flag if -2147483648 < res*flag < 2147483647 else 0)
    return res*flag if -2147483648 < res*flag < 2147483647 else 0
reverse(1534236469)


