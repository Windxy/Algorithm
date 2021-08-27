# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （双指针）三数之和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/19 10:05
**************************************************
'''
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
思路（脑海里记得有一幅图）：
0.初始判断，如果为空，返回[]
1.排序（目的在于能够进行下标游走）
2.设置三个下标进行游走，l，i，r
初始化l,r
3.如果l没有碰到r，则进行下列操作
    3.1 初始化i=l+1
    3.2 如果i没有碰到r，则进行下列操作
        3.2.1 如果 a[i]+a[l]+a[r]<0 则 i 右移，因为a是低到高排序的
        3.2.2 如果 a[i]+a[l]+a[r]==0，保存这个结果，并让l=l+1，跳过此循环
        3.2.3 如果 a[i]+a[l]+a[r]>0 则 r 左移，理由同上
4.返回所有结果
'''
class Solution:
    def threeSum(self, nums: [int]) -> [[int]]:
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j: # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

# 作者：jyd
# 链接：https://leetcode-cn.com/problems/3sum/solution/3sumpai-xu-shuang-zhi-zhen-yi-dong-by-jyd/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

