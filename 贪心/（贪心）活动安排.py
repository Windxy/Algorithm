'''
ACM格式
题源：https://ac.nowcoder.com/acm/contest/950/A
'''
n = int(input())

ans = []
for i in range(n):
    ints = list(map(int,input().split()))
    ans.append(ints)

ans = sorted(ans,key=lambda x:x[1])

# 遍历
end = 0     #结束时间
count = 0   #计数
for num in ans:
    # 获取第一个最小的开始时间，并重新赋值结束时间
    # 滚动方法类似于斐波拉契算法的动态规划
    if num[0] >= end:
        end = num[1]
        count += 1
print(count)