# coding:utf-8
'''
**************************************************
@File   ：python_dp -> 盛最多水的容器
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/16 8:35
**************************************************
'''
'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def maxArea(height:list) -> int:
    i=0;j=len(height)-1
    ans = 0
    while(i!=j):
        ans = max(ans,min(height[i],height[j])*(j-i))
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    print(ans)
    pass

l = [1,8,6,2,5,4,8,3,7]
maxArea(l)