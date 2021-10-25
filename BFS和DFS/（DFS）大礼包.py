''''''
'''在 LeetCode 商店中， 有 n 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。

给你一个整数数组 price 表示物品价格，其中 price[i] 是第 i 件物品的价格。另有一个整数数组 needs 表示购物清单，其中 needs[i] 是需要购买第 i 件物品的数量。

还有一个数组 special 表示大礼包，special[i] 的长度为 n + 1 ，其中 special[i][j] 表示第 i 个大礼包中内含第 j 件物品的数量，且 special[i][n] （也就是数组中的最后一个整数）为第 i 个大礼包的价格。

返回 确切 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shopping-offers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        N = len(needs)

        #深度优先遍历 + 按条件筛选 +记忆化搜索
        @lru_cache(None)
        def dfs(cur_need):
            min_ans = sum(data * price[idx] for idx,data in enumerate(cur_need))
            for sp in special:
                ok = True
                for i in range(N):
                    if sp[i] > cur_need[i]:
                        ok = False
                        break
                if ok:
                    temp = [data - sp[idx] for idx,data in enumerate(cur_need)]
                    min_ans = min(min_ans,dfs(tuple(temp))+sp[-1])
            return min_ans

        ans = dfs(tuple(needs))
        print(ans)
        return ans
S = Solution()
ans = S.shoppingOffers(price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2])
