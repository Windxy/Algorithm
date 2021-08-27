from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.que = nums
        heapq.heapify(self.que) #self.que转为堆

    def add(self, val: int) -> int:
        heapq.heappush(self.que,val)
        while len(self.que)>self.k:
            heapq.heappop(self.que)
        return self.que[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)