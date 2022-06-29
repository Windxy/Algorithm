class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针
        L = 0   # 移动针
        R = 0 # 判断是否为非0针
        while L<len(nums):
            if nums[L]==0:
                # 找到L右边第一个非零元素
                while R <= L:
                    R += 1
                while R < len(nums):
                    if nums[R]==0:
                        R+=1
                    else:
                        break
                if R==len(nums):
                    return
                # 交换
                nums[L],nums[R] = nums[R],nums[L]
            L+=1
        return
if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0,1,0,3,12])