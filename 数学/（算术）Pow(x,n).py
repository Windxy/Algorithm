# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （算术）Pow(x,n)
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/13 15:48
**************************************************
'''
'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
示例 1:
输入: 2.00000, 10
输出: 1024.00000
示例 2:
输入: 2.10000, 3
输出: 9.26100
示例 3:
输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def myPowHelper(self,x,n):
        if n==1:
            return x
        if n%2 == 1 :
            tmp = self.myPowHelper(x,n//2)
            return tmp*tmp*x
        if n%2 == 0 :
            tmp = self.myPowHelper(x,n//2)
            return tmp*tmp


    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1

        if n<0:
            return 1/self.myPowHelper(x,-n)

        return self.myPowHelper(x,n)

s = Solution()
s.myPow(2,10)