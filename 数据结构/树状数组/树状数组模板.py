'''https://leetcode-cn.com/circle/article/OeMXPy/'''
'''
树状数组或二叉索引树（英语：Binary Indexed Tree），又以其发明者命名为 Fenwick 树。
其初衷是解决数据压缩里的累积频率（Cumulative Frequency）的计算问题，现多用于高效计算数列的前缀和，区间和。
它可以以O(logN)的时间得到任意前缀和，并同时支持在 O(logN) 时间内支持动态单点值的修改。空间复杂度O(n)。

树状数组的基本功能是：1.单点增加 2.前缀查询
树状数组的典型问题：区间和的个数，逆序数对

先验知识：
1.lowbit（低位）运算：
lowbit(n) 定义为非负整数 n 在二进制表示下 “最低位的 1 及其后边所有的 0” 所构成的数值。
例如：n=12，bit(12) = 1100，则lowbit(12) = 100，就等于4
通用公式：lowbit(n) = n&(~n+1) = n&(-n)，反码+1即为补码

2.如何计算整数n在二进制表示下，1的位数
比如要求bit(12) = 1100，1的位数分别是3，4
step0.初始化n = 12
step1.第一个是lowbit(n) = 4, 第一个1的位数就是log4 = 2，存下来，这里log底数取2
step2.n = n - lowbit(n)      # 比如，12-lowbit(12) = 12 - 4 = 8，在二进制表示上，就是将第一位为1的数置零了
step3.判断 n 是否等于0,如果不是，那么step1，否则step4
step4.返回所有1的位数

优化：可以考虑在取log的时候，将其预先用哈希进行存储，节省时间

3.整数可以表示成为n = 2^i_1 + 2^i_2 + ... + 2^i_m，其中，i表示整数在二进制表示下，1的位数，假设i_1 > i_2，以此类推


'''


class BitTree:  # 树状数组 动态前缀和
    def __init__(self, n):
        self.tree = [0 for x in range(n + 1)]
        self.n = n

    # ---- 最右侧1的权重
    def lowbit(self, i: int) -> int:
        return i & (-i)

    # ----某个位置，加上k
    def update(self, i: int, k: int) -> None:
        while i <= self.n:
            self.tree[i] += k
            i += self.lowbit(i)

    # ----前缀和（实指）
    def presum(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= self.lowbit(i)
        return res

from typing import List
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        # ---- 前缀和 实指
        presum = [0 for _ in range(n + 1)]
        for i in range(n):  # 虚指
            presum[i + 1] = presum[i] + nums[i]
            # ------------------ 以presum 为对象  离散化 + 树状数组----------------------#
        # ------ 所有的点
        all_num = []
        for x in presum:
            all_num += [x, x - lower, x - upper]

        # ------ 离散化
        all_num = list(set(all_num))    #离散化，要去重 都行
        all_num.sort()  # 排序

        val_id = dict()
        for i, x in enumerate(all_num):
            val_id[x] = i
        # ------ 树状数组
        BIT = BitTree(len(all_num))
        res = 0
        for i, x in enumerate(presum):  # 遍历，往前探
            idL = val_id[x - upper]
            idR = val_id[x - lower]
            res += (BIT.presum(idR + 1) - BIT.presum(idL + 1 - 1))

            ID = val_id[x]
            BIT.update(ID + 1, 1)
        print(res)
        return res

nums = [-2,5,-1]
lower = -2
upper = 2
s = Solution()
s.countRangeSum(nums,lower,upper)

# 作者：Hanxin_Hanxin
# 链接：https: // leetcode - cn.com / problems / count - of - range - sum / solution / c - python3 - tao - gui - bing - pai - xu - mo - ban - qia - 5l
# 87 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。