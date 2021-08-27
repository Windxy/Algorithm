'''
小朋友 A 在和 ta 的小伙伴们玩传信息游戏，游戏规则如下：
有 n 名玩家，所有玩家编号分别为 0 ～ n-1，其中小朋友 A 的编号为 0
每个玩家都有固定的若干个可传信息的其他玩家（也可能没有）。传信息的关系是单向的（比如 A 可以向 B 传信息，但 B 不能向 A 传信息）。
每轮信息必须需要传递给另一个人，且信息可重复经过同一个人
给定总玩家数 n，以及按 [玩家编号,对应可传递玩家编号] 关系组成的二维数组 relation。返回信息从小 A (编号 0 ) 经过 k 轮传递到编号为 n-1 的小伙伴处的方案数；若不能到达，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/chuan-di-xin-xi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
'''
输入：n = 5, relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]], k = 3
输出：3
解释：信息从小 A 编号 0 处开始，经 3 轮传递，到达编号 4。共有 3 种方案，分别是 0->2->0->4， 0->2->1->4， 0->2->3->4。
'''
from typing import List
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        '''k>0'''
        '''
        动态规划：i+1时刻状态与i时刻状态有关，设dp[i][j]为第i轮传递，到编号j的方案数
        有：dp[i][dst] = Σdp[i-1][src]，src和dst满足（src,dst）∈relation
        最后返回dp[k][n-1]
        边界条件为：
        dp[0][dst] = 0 if dst != 0 else 1
        '''
        # step1.初始化以及设置初始边界条件
        dp = [[0]*(n+1) for _ in range(k+1)]
        dp[0][0] = 1
        # step2.状态转移
        for i in range(k):        #时刻
            for edge in relation:
                src = edge[0]
                dst = edge[1]
                dp[i+1][dst] += dp[i][src]
        print(dp[k][n-1])
        return dp[k][n-1]

n = 5
relation = [[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]]
k = 3
so = Solution()
so.numWays(n,relation,k)