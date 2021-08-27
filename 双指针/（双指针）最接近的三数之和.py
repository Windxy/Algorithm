# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （双指针）最接近的三数之和
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/19 13:10
**************************************************
'''
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def threeSumClosest(self, nums: [int],target: int) -> [[int],]:
        '''
        :param nums:
        :param target:
        :return:
        '''
        '''3 <= nums.length <= 10^3'''
        nums.sort()
        min = nums[1]+nums[0]+nums[2]  #初始化一下
        for k in range(len(nums) - 2):
            i, j = k + 1, len(nums) - 1
            while i < j:
                tmp = nums[k]+nums[i]+nums[j]
                if abs(tmp-target)<abs(min-target): #距离更小，更适合
                    min = tmp
                if tmp<target:#此时小，i右移
                    i+=1
                elif tmp>target:#此时大，j左移
                    j-=1
                else:       # 否则，怎么移动都没啥用
                    return tmp
        print(min)
        return min
s = Solution()
s.threeSumClosest([-1,2,1,-4],1)