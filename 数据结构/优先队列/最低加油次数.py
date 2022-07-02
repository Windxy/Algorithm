import heapq
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations) -> int:
        # 评论1.只要现在需要加油，并且前面有加油站，那么此时就可以加油
        # 评论2.路上的不是加油站，而是一桶桶的油，每次经过的时候，就把油带上，当油不够的时候我们就取身上最大的那桶油加上，这样如果身上没油了，那么就到不了了
        array = []
        # heapq.heapify(array) # 将array堆化
        # heapq默认小顶堆，如果数值取反，即原来数的负数，则可以构造大顶堆
        if startFuel >= target:
            return 0
        ret = 0
        idx = 0
        while startFuel < target:
            while idx < len(stations) and startFuel >= stations[idx][0]: # 不断加油(同时保证车上有油的情况)，直到没有油
                stop,fuel = stations[idx][0],stations[idx][1]
                heapq.heappush(array,-fuel)
                idx += 1
            # 没有油，加油，直到有油（下一步），或者没有油了（-1返回）
            if array == []:
                return -1
            startFuel += abs(heapq.heappop(array))
            ret += 1
        return -1

