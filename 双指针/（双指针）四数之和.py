# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （双指针）四数之和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/21 16:25
**************************************************
'''
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, k = [], 0
        for m in range(len(nums)-3):
            # if nums[m]>target:break       #因为有负数，所以不能这样
            if m>0 and nums[m]==nums[m-1]:continue
            for k in range(m+1,len(nums) - 2):
                # if nums[k] > target: break # 1. because of j > i > k.
                if k > m+1 and nums[k] == nums[k - 1]: continue # 2. skip the same `nums[k]`.
                i, j = k + 1, len(nums) - 1
                while i < j: # 3. double pointer
                    s = nums[k] + nums[i] + nums[j] + nums[m]
                    if s < target:
                        i += 1
                        while i < j and nums[i] == nums[i - 1]:     # 去重
                            i += 1
                    elif s > target:
                        j -= 1
                        while i < j and nums[j] == nums[j + 1]:     # 去重
                            j -= 1
                    else:
                        res.append([nums[m],nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i - 1]:
                            i += 1
                        while i < j and nums[j] == nums[j + 1]:
                            j -= 1
        return res

    def fourSum2(self,nums,target):
        nums.sort()
        ans = []
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a-1]:continue  #去重
            for b in range(a+1,len(nums)-2):
                if b > a+1 and nums[b] == nums[b-1]:continue
                c, d = b + 1, len(nums) - 1
                while c < d:
                    tmp = nums[a] + nums[b] + nums[c] + nums[d]
                    if target > tmp:
                        c = c + 1
                        while c<d and nums[c] == nums[c-1]:c = c + 1
                    elif target < tmp:
                        d = d - 1
                        while c<d and nums[d] == nums[d+1]:d = d - 1
                    else:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        c = c + 1
                        d = d - 1
                        while c<d and nums[c] == nums[c-1]:c = c+1
                        while c<d and nums[d] == nums[d+1]:d = d-1
        return ans
s = Solution()
# print(s.fourSum2([1,-2,-5,-4,-3,3,3,5],-11))
print(s.fourSum2([-2,-1,-1,1,1,2,2],0))