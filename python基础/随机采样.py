# https://blog.csdn.net/u014636245/article/details/103512111
import random
N = range(1324)
m = 324
a = random.sample(N, m)
b = set()
for num in a:
    if num in b:
        print("wrong")
        break
    b.add(num)
