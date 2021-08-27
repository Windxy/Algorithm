from collections import OrderedDict
class Solution:
    def __init__(self):
        self.cache = OrderedDict()
        self.k = 0

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)#如果用过了，就优先放在最后，然后重新赋值
        self.cache[key] = value
        if len(self.cache) > self.k:
            self.cache.popitem(last=False)

    def LRU(self, operators, k):
        res = []
        self.k = k
        for opt in operators:
            if opt[0] == 1:
                self.set(opt[1], opt[2])
            elif opt[0] == 2:
                res.append(self.get(opt[1]))
        return res
opreators = [[1,1,1],[1,2,2],[1,3,2],[2,1],[1,4,4],[2,2]]
k = 3

s = Solution()
print(s.LRU(opreators,k))