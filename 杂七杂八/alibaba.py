
# num = str(input())
#
# N = 0
# for char in num:
#     N = max(int(char)+1,N)
#
# def Kto10(num,K):
#     ans = 0
#     for i in num:
#         ans = (ans * K + int(i))%(10**9+7)
#     return ans
#
# for K in range(N,17):
#     print(Kto10(num,K))
#     # print(int(num,K)%(10**9+7))
#
# '''
# 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
# 651155393
# 587201601
# 59213536
# 999622471
# 593485973
# 545282109
# 92033093
# '''
#

import sys
import collections
readline = sys.stdin.readline


def readstr() -> str:
    return readline().strip()


s = readstr()
if s == "0" * len(s):
    print(0)
else:
    s_list = list(s)
    counter = collections.Counter(s)
    max_num = max(s_list)
    hashmap = {"F": 16,
               "E": 15,
               "D": 14,
               "C": 13,
               "B": 12,
               "A": 11,
               "9": 10,
               "8": 9,
               "7": 8,
               "6": 7,
               "5": 6,
               "4": 5,
               "3": 4,
               "2": 3,
               "1": 2
               }
    index = hashmap[max_num]
    ans = set()
    MOD = 10 ** 9 + 7
    for i in range(index, 17):
        temp = int(s, i)
        temp %= MOD
        ans.add(temp)
    sorted_ans = sorted(ans)
    for i in range(len(sorted_ans)):
        print(sorted_ans[i])