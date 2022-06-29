class two_list_node():
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


# 双向链表（非循环） + 哈希
# map：节点
class LRUCache:
    def __init__(self, capacity: int):
        self.wln_first = two_list_node(-1, -1)  # 定义一个值为-1的哑节点的双向链表作为初始化
        self.wln_last = two_list_node(-1, -1)  # 定义一个值为-1的哑节点的双向链表作为初始化
        self.wln_first.right = self.wln_last
        self.wln_last.left = self.wln_first
        '''
        节点_firt <--> 节点_last
        '''
        self.s = {}  # key-->node(存的是val)
        self.capacity = capacity

    def get(self, key: int) -> int:

        if key not in self.s:
            # print(-1)
            return -1

        # 最近使用了，因此需要把它放在最前面
        tmp_n = self.s[key]
        tmp_n.left.right = tmp_n.right
        tmp_n.right.left = tmp_n.left
        # 然后再加上它
        tmp = two_list_node(key, tmp_n.val)
        tmp.right = self.wln_first.right
        self.wln_first.right.left = tmp
        self.wln_first.right = tmp
        tmp.left = self.wln_first
        self.s[key] = tmp
        return self.s[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.s:  # 存储区中没有该节点
            # 先判断有没有超过范围，如果有超过，就删掉它
            if len(self.s) == self.capacity:
                tmp = self.wln_last.left
                self.wln_last.left = tmp.left
                tmp.left.right = self.wln_last
                self.s.pop(tmp.key)
            tmp = two_list_node(key, value)
            tmp.right = self.wln_first.right
            self.wln_first.right.left = tmp
            self.wln_first.right = tmp
            tmp.left = self.wln_first
            self.s[key] = tmp
        else:  # 存储区中有该节点，先删掉它
            tmp_n = self.s[key]
            tmp_n.left.right = tmp_n.right
            tmp_n.right.left = tmp_n.left
            # 然后再加上它
            tmp = two_list_node(key, value)
            tmp.right = self.wln_first.right
            self.wln_first.right.left = tmp
            self.wln_first.right = tmp
            tmp.left = self.wln_first
            self.s[key] = tmp

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    LRU = LRUCache(2)
    print(LRU.put(1,1),end=' ')
    print(LRU.put(2,2),end=' ')
    print(LRU.get(1),end=' ')
    print(LRU.put(3,3),end=' ')
    print(LRU.get(2),end=' ')
    print(LRU.put(4,4),end=' ')
    print(LRU.get(1),end=' ')
    print(LRU.get(3),end=' ')
    print(LRU.get(4),end=' ')