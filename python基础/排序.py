a = [1,3,4,2,5]
a = sorted(a)
print(a)

b = [[10,30],[20,60],[80,100],[150,180]]
b = sorted(b,key=lambda x:(x[0],[1]))
print(b)

import functools

def sort_rule(x,y):
    if x+y < y+x:
        return 1
    elif x+y > y+x:
        return -1
    else:
        return 0

a = [3,30,34,5,9]
a = [str(i) for i in a]
a = sorted(a,key=functools.cmp_to_key(sort_rule))