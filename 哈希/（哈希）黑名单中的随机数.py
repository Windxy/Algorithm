'''
给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的整数。
任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。
优化你的算法，使它最小化调用语言 内置 随机函数的次数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/random-pick-with-blacklist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        '''
        0 1 2 3 4 5 6
        黑[2 3 5]
        非黑[0 1] [4 6]

        找到1.黑[2 3] 2.非黑[4 6]

        因此映射关系为:2--4  3--6
        '''
        self.N =  n - len(blacklist) # 只有N个有效名单,7-3=4
        black = {b_num for b_num in blacklist if b_num <self.N}
        non_black = {*range(self.N ,n)} - set(blacklist)
        # 构建映射关系
        self.map = {k :v for k ,v in zip(black ,non_black)}

    def pick(self) -> int:
        r = randint(0 ,self. N -1)
        return r if r not in self.map else self.map[r]



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()