# 每个数最多两次出现
from typing import List
class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        nums = sorted(nums)#排序
        flag_num = nums[0]
        times = 1
        idx = 1
        while idx<len(nums):
            if flag_num == nums[idx]:       # 如果还是一样的，则time加1，flag_num不变
                times += 1
            else:                           # 如果不一样了，则time=1，flag_num更新
                flag_num = nums[idx]
                times = 1
            if times == 3:
                nums.pop(idx)
            idx += 1
        print(nums)
        print(len(nums))
        return len(nums)

    def removeDuplicates(self, nums: List[int]) -> int:
        j = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[j - 2]:
                nums[j] = nums[i]
                j += 1
        return j

s = Solution()
list_a = [1,1,1,2,2,3]
s.removeDuplicates(list_a)