'''参考资料：https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/'''
'''
并查集，顾名思义就是能够实现合并、查找的集合，是一种特殊的数据结构
并查集与树很像，但是树一般记录节点的子节点，而并查集一般记录节点的父节点
并查集的基本功能是：1.合并  2.查找
并查集的典型应用：判断任意两个人是否具有亲属关系，判断有多少个连通分量
'''
class UnionFindSet():
    def __init__(self):
        '''记录父节点'''
        self._father = {}   #比如：节点4的父节点是3，则有：father = {4:3};在新插入一个新的节点时候，需要赋值父节点为None

    def find(self,x):
        '''
        查找祖先节点，用于判断两个节点是否属于同一个集合下
        :return:root
        '''
        root = x
        while self._father[root] is not None:
            root = self._father[root]

        '''
        在查找过程中，可以进行路径压缩
        如果我们树很深，比如说退化成链表，那么每次查询的效率都会非常低。所以我们要做一下路径压缩。也就是把树的深度固定为二
        '''
        while root != x:
            temp = self._father[x]
            self._father[x] = root
            x = temp

        return root

    def merge(self,x,y):
        '''
        合并两个节点
        :return:x作为y的父节点
        '''
        root1 = self.find(x)
        root2 = self.find(y)
        if root1 != root2:
            self._father[root2] = root1

    def isConnect(self,x,y):
        '''
        判断两个节点是否连通
        :return: T或F
        '''
        return self.find(x) == self.find(y)

    def add(self,x):
        if x not in self._father:
            self._father[x] = None