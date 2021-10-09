from sortedcontainers import SortedList,SortedDict,SortedSet
sl = SortedList(['e', 'a', 'c', 'd', 'b'])
sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
print(sd)
print(sl)

# 有序字典
# 可自动排序key值
SL = SortedList()
SL.add(1)
SL.add(-1)
SL.add(4)
print(list(SL))