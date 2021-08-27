# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 两数之和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/10 15:18
**************************************************
'''
'''给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 哈希
from typing import List
class Solution:
    def twoSum(self, candidates: List[int], target: int) -> List[List[int]]:
        hash = {}
        for i,j in enumerate(candidates):
            if j in hash.keys():
               return [hash[j],i]
            hash[target-j]=i

s = Solution()
print(s.twoSum([2,7,11,15],9))
