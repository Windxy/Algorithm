# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （回溯）子集2
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/20 15:26
**************************************************
'''
'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def subset(nums):
    ans = []
    nums = sorted(nums)
    def helper(num,l):
        ans.append(l)
        for i in range(len(num)):
            if i>0 and num[i]==num[i-1]:   # 如果现在取这个值和前面的值一样了，就不用放进去
                continue
            helper(num[i+1:],l+[num[i]])
        return ans

    helper(num = nums,l = [])

    print(ans)
    return ans

subset([4,4,4,1,4])