''''''

'''
你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。
你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。
如果你能使这个正方形，则返回 true ，否则返回 false 。

示例 1:
输入: matchsticks = [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: matchsticks = [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/matchsticks-to-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

'''回溯'''

from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # 回溯
        edges = [0] * 4

        def dfs(idx):
            if idx == len(matchsticks):
                return True
            for i in range(4):
                edges[i] += matchsticks[idx]
                if edges[i] <= edge and dfs(idx + 1):
                    return True
                edges[i] -= matchsticks[idx]
            return False
            # pass

        all_num = sum(matchsticks)
        if all_num % 4 != 0 or all_num < 4:
            return False
        matchsticks.sort(reverse=True)
        edge = all_num // 4

        return True if dfs(0) else False