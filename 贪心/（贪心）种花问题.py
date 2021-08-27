# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （贪心）种花问题
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2021/1/1 20:50
**************************************************
'''
'''
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。
示例 1:
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-place-flowers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
'''思路：如果前后中，都是0，则可以种植，最后看n的正负即可'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1,len(flowerbed)-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
        return False if n>=1 else True

