# import random
# # 0.2~0.5的随机数
# Ans = random.randint(200,500)/1000.0
# print(Ans)

#随机取样
import random
for i in range(10):
    N = range(50)
    m = 9
    a = random.sample(N, m)
    print(a)
