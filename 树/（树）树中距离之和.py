# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （树）树中距离之和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/6 15:16
**************************************************
'''
'''
给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
返回一个表示节点 i 与其他所有节点距离之和的列表 ans。
示例 1:

输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释: 
如下为给定的树的示意图：
  0
 / \
1   2
   /|\
  3 4 5

我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-distances-in-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        for baba, erza in edges:
            tree[baba].append(erza)
            tree[erza].append(baba)
        depth = [0 for _ in range(N)]
        count = [0 for _ in range(N)]


        def dfsForDepthAndCount(baba0, father):
            count[baba0] = 1
            for erza0 in tree[baba0]:
                if erza0 != father:
                    depth[erza0] = depth[baba0] + 1
                    dfsForDepthAndCount(erza0, baba0)
                    count[baba0] += count[erza0]


        dfsForDepthAndCount(0, -1)
        answer = [0 for _ in range(N)]
        answer[0] = sum(depth)


        def dfsForAnswer(baba1, father):
            for erza1 in tree[baba1]:
                if erza1 != father:
                    answer[erza1] = answer[baba1] + N - 2 * count[erza1]
                    dfsForAnswer(erza1, baba1)


        dfsForAnswer(0, -1)
        return answer

N = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]

s = Solution()
s.sumOfDistancesInTree(N,edges)
# 作者：flying_du
# 链接：https://leetcode-cn.com/problems/sum-of-distances-in-tree/solution/python-zui-qiang-da-an-zhu-shi-si-lu-qing-xi-fei-y/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处