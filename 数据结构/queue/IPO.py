# https://leetcode-cn.com/problems/ipo/
from heapq import *
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 贪心
        project = list(zip(capital,profits))
        project.sort()
        curr = 0

        n = len(profits)
        pq = []
        for i in range(k):
            while curr < n and w >= project[curr][0]:
                heappush(pq,-project[curr][1]) # 因为python的heap只pop最小值，因此加上负号
                curr += 1
            if pq:
                w -= heappop(pq)
            else:
                break
        return w