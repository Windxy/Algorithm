import numpy as np

# 获取排序的索引号
array = np.random.random(size=(1,10))
array_sort = array.argsort()

print(array)
print(array_sort)


# 获取多个数组的最值
array1 = np.random.random(size=(1,1))
array2 = np.random.random(size=(1,5))
yy2 = np.minimum(array1, array2)
print(array1)
print(array2)
print(yy2)
