import random
import numpy as np
import time

# 输入一个平均值A
# 输出15个1~5的随机数，15个数的平均值为A
def get_15_nums(mean_num):
    ret = []
    while True:
        ret.clear()
        for i in range(14):
            # 1~5的随机数
            r_num = random.randint(10000, 50000) / 10000
            ret.append(r_num)

        if 1 <= 15*mean_num-sum(ret) <= 5:
            ret.append( 15 * mean_num - sum(ret) )
            break
    return ret

# ret = get_15_nums(2.4224)
# ret = list(map(float("%.4f"%ret),ret))
# print(ret)
def func(nums):
    return round(nums,4)
    # return float("%.4f" % nums)
nums = [2.3769, 1.8643, 1.2752, 2.4563, 3.3025,2.1191, 1.2688, 1.4376, 3.3029, 2.6788]

i = 4
ret = get_15_nums(nums[i])
print("mean",sum(ret)/15)
# ret = list(map(func,ret))
print('{0}个数组为,{1}'.format(i+1,ret))
