# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）第K个排列
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/23 9:37
**************************************************
'''
'''
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:
输入: n = 3, k = 3
输出: "213"
示例 2:
输入: n = 4, k = 9
输出: "2314"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l = []
        for i in range(n):
            l.append(i+1)
        ans = self.permute(l)
        tmp = ans[k-1]
        def strs(x):
            return str(x)
        tmp = map(strs,tmp)
        print(''.join(tmp))
    def permute(self, nums):
        ans = []

        def search(left, history):
            # nonlocal ans
            if not left:
                ans.append(history)
                return

            for i in range(len(left)):
                search(left[:i] + left[i + 1:], history + [left[i]])

        search(nums, [])
        # print(ans)
        return ans
s = Solution()
s.getPermutation(4,9)


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        s, k, res = list(range(1, n+1)), k-1, ""
        for i in range(len(s)-1, -1, -1):
            # res, s, k = res+str(s[k // factorial(i)]), s[:k // factorial(i)]+s[k // factorial(i)+1:], k % factorial(i)
            pass
        return res

# 作者：ting-ting-28
# 链接：https://leetcode-cn.com/problems/permutation-sequence/solution/python3-chao-xiang-xi-duo-jie-fa-by-ting-ting-28-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。