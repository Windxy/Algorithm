# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 组合总和2（回溯）
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/10 14:10
**************************************************
'''
'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        path = []

        def helper(target, begin, path):
            if target == 0:
                res.append(path)
                return
            if target < 0 :
                return
            for i in range(begin,len(candidates)):
                if target-candidates[i]<0 :
                    break #后面都可以不要
                helper(target-candidates[i], i+1, path+[candidates[i]])
            return res
        # 想办法去重
        helper(target,0,path)

        a = [];
        for i in res:
            if i not in a:
                a.append(i)
        return a
candidates = [10,1,2,7,6,1,5]
target = 8
s= Solution()
s.combinationSum2(candidates,target)

'''别人的'''
from typing import List
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(begin, path, residue):
            if residue == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                if candidates[index] > residue:
                    break

                if index > begin and candidates[index - 1] == candidates[index]:
                    continue

                path.append(candidates[index])
                dfs(index + 1, path, residue - candidates[index])
                path.pop()

        size = len(candidates)
        if size == 0:
            return []

        candidates.sort()
        res = []
        dfs(0, [], target)
        return res

# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/combination-sum-ii/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-m-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。