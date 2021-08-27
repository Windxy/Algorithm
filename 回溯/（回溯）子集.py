# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）子集
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/20 15:10
**************************************************
'''
'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def subset(nums):
    ans = []

    def helper(num,lis):
        nonlocal ans
        ans.append(lis)

        for i in range(len(num)):
            helper(num[i+1:],lis+[num[i]])
        return

    helper(nums, [])

    print(ans)
    return ans

subset([1,2,3])