#https://leetcode-cn.com/problems/paint-house-iii/solution/python3ji-bai-shuang-bai-dai-ma-by-dreamcatcher_/
from typing import List
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def dfs(idx, color, t):
            if t < 0 or t > m - idx:
                return float("inf")
            if idx == m:
                return 0
            curr = float("inf")
            if houses[idx]:
                if houses[idx] != color:
                    curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
                else:
                    curr = min(curr, dfs(idx + 1, houses[idx], t))
            else:
                for i in range(1, n + 1):
                    if i != color:
                        curr = min(curr, dfs(idx + 1, i, t - 1) + cost[idx][i - 1])
                    else:
                        curr = min(curr, dfs(idx + 1, i, t) + cost[idx][i - 1])
            return curr

        res = dfs(0, 0, target)
        if res == float("inf"):
            return -1
        return res

# 作者：AC_OIer
# 链接：https://leetcode-cn.com/problems/paint-house-iii/solution/gong-shui-san-xie-san-wei-dong-tai-gui-h-ud7m/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。