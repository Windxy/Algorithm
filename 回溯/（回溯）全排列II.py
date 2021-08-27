# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）全排列II
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/18 18:17
**************************************************
'''
'''
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def search(left,history):
            nonlocal ret
            if not left: #如果没有可以搜的了，说明所有数字用完了
                ret.append(history)

            for i in set(left): # 只考虑了当前位置不重复选择，那也就能保证history不重复，所以直接用一个集合来维护
                left.remove(i)
                left.append(i)
                search(left[:-1],history+[i])

        search(nums,[])
        print(ret)
        return ret

s = Solution()
s.permuteUnique([1,1,1,2,2,2,])