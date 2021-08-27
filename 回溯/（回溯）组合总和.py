# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 组合总和（回溯）
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/9 14:42
**************************************************
'''
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []

        def bfs(begin,target,path):
            if target < 0:
                return # 不符合
            if target == 0:
                ans.append(path) # 保存
                return
            for i in range(begin,len(candidates)):
                bfs(i,target-candidates[i],path+[candidates[i]])

        if len(candidates)==0:return
        bfs(0,target,path)
        return ans

s = Solution()
print(s.combinationSum(candidates=[2,3,6,7],target=7))
