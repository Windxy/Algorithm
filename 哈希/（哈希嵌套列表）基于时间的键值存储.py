'''https://leetcode-cn.com/problems/time-based-key-value-store/'''
from collections import defaultdict
class TimeMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = defaultdict(list)

    def set(self, key, value, timestamp):
        self.data[key].append([timestamp, value])   #重点在于设计数据结构和查找方法

    def getIndex(self, nums, timestamp):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid][0] < timestamp:
                left = mid + 1
            elif nums[mid][0] > timestamp:
                right = mid - 1
            else:
                return mid

        return right

    def get(self, key, timestamp):
        # ind = bisect_left(self.d[key], (timestamp+1, ))-1
        key_data = self.data[key]
        ind = self.getIndex(key_data, timestamp)
        return key_data[ind][1] if ind >= 0 else ""