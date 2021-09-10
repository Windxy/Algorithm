import bisect

a = [1,3,5,7,9,11]
idx1 = bisect.bisect_left(a,5)  # 2 # 如果要插入5，left方法会返回idx为2
idx2 = bisect.bisect_right(a,1) # 3 # 如果要插入5，right方法会返回idx为2
print(idx1,idx2)
idx1 = bisect.bisect_left(a,6)  # 3
idx2 = bisect.bisect_right(a,6) # 3
print(idx1,idx2)
idx1 = bisect.bisect_left(a,0)  # 0
idx2 = bisect.bisect_right(a,0) # 0
print(idx1,idx2)