# num = str(input())
# dic = {'0':1,'1':0,'2':0,'3':0,'4':0,'5':0,'6':1,'7':0,'8':2,'9':1}
#
# ans = 0
# for char in num:
#     ans += dic[char]
# print(ans)

# N = int(input())
# highs = list(map(int,input().split()))
# names = input().split()
#
# lists = [[h,n] for h,n in zip(highs,names)]
#
# lists = sorted(lists,key=lambda x:(x[0],x[1]))
# for a,b in lists:
#     print(b,end=' ')

# n,m = list(map(int,input().split()))
# dic = set()
# N_a = input().split()
# N_b = input().split()
# for a,b in zip(N_a,N_b):
#     dic.add((a,b))
# times = int(input())
# for i in range(times):
#     q_a,q_b = input().split()
#     if (q_a,q_b) in dic or (q_b,q_a) in dic:
#         print("Yes")
#     else:
#         print("No")
'''
4 5 
1 2 1 3 1
2 1 3 2 4
4
1 2
2 4
2 3
1 4
'''

MOD = 10**9 + 7

n = int(input())
ans = n*(n*n+3-3*n)*(n-1)
print(ans%MOD)

