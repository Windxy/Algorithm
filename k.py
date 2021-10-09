from functools import cmp_to_key

def compare(s1, s2):
    if float(s1[0]) > float(s2[0]):
        return 1
    if float(s1[0]) < float(s2[0]):
        return -1
    if float(s1[0]) == float(s2[0]):
        if float(s1[1]) > float(s2[1]):
            return 1
        if float(s1[1]) < float(s2[1]):
            return -1
        if float(s1[1]) == float(s2[1]):
            if float(s1[2]) > float(s2[2]):
                return 1
            if float(s1[2]) < float(s2[2]):
                return 0

def print_ans(strs:list):
    arr = [i.split(':') for i in strs]
    newarr = sorted(arr,key=cmp_to_key(compare))
    ans = []
    for k in newarr:
        ans.append('{0}.{1}.{2}'.format(k[0],k[1],k[2]))
    return ans

ans = []
N = int(input())
while N:
    N-=1
    ans.append(input())
ans = print_ans(ans)
for i in ans:
    print(i)
'''
2
01:41:8.9
1:1:09.211

3
23:41:08.023
1:1:08.211
08:01:22.0

2
22:41:08.023
22:41:08.23
'''