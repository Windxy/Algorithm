# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 两数之和3（回溯）
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/11 10:07
**************************************************
'''
'''找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。'''
'''所有数字都是正整数。解集不能包含重复的组合'''
'''
输入: k = 3, n = 7
输出: [[1,2,4]]
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
'''

from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        candidates = [i for i in range(1,10)]

        def bfs(target,begin,path,num):
            if target<0:    #似乎用不上
                return
            if target==0 and k==num:
                res.append(path)
                return

            for i in range(begin,9):
                if target-candidates[i]<0:  # 剪掉        0
                    continue
                num += 1
                bfs(target-candidates[i],i+1,path+[candidates[i]],num)
                num -= 1

        bfs(n,0,path,0)
        return res

k = 3; n = 7
s = Solution()
print(s.combinationSum3(k,n))

