N = int(input())
if N == 0:
	print(0)
	exit()
maxtrix = [[0] * N for _ in range(N)]
for i in range(N):
	a,b,c = map(int,input().split())
	maxtrix[a-1][b-1] = c

dp = [[maxtrix[0][0]]*N for _ in range(N)]
# 初始化dp
for i in range(1,N):
	dp[i][0] = dp[i-1][0] + maxtrix[i][0]
	dp[0][i] = dp[0][i-1] + maxtrix[0][i]
# 得到最值Mr.Ming
for i in range(1,N):
	for j in range(1,N):
		dp[i][j] = max(dp[i-1][j],dp[i][j-1])+maxtrix[i][j]

# 逆推
ans_Ming = dp[-1][-1]
cur_i,cur_j = N-1,N-1
while not (cur_i==0 and cur_j==0):
	cur_score = dp[cur_i][cur_j]
	# 跳转优先
	if cur_i>0 and cur_j>0 and dp[cur_i][cur_j] > dp[cur_i-1][cur_j] and dp[cur_i][cur_j] > dp[cur_i][cur_j-1]:
		maxtrix[cur_i][cur_j] = 0
		if dp[cur_i-1][cur_j]>dp[cur_i][cur_j-1]:
			cur_i -= 1
		else:
			cur_j -= 1
		continue
	if cur_i==0 and cur_j>0 and dp[cur_i][cur_j]>dp[cur_i][cur_j-1]:
		maxtrix[cur_i][cur_j] = 0
		cur_j -= 1
		continue
	if cur_j == 0 and cur_i>0 and dp[cur_i][cur_j]>dp[cur_i-1][cur_j]:
		maxtrix[cur_i][cur_j] = 0
		cur_i -= 1
		continue
	# 未跳转
	if cur_i-1 >=0 and cur_score == dp[cur_i-1][cur_j]:
		cur_i -= 1
	elif cur_j >= 0 and cur_score == dp[cur_i][cur_j-1]:
		cur_j -= 1

dp = [[0]*N for i in range(N)]
# 初始化
for i in range(1,N):
	dp[0][i] = dp[0][i-1] +maxtrix[0][i]
	dp[i][0] = dp[i-1][0] + maxtrix[0][i]
for i in range(1,N):
	for j in range(1,N):
		dp[i][j] = max(dp[i-1][j],dp[i][j-1])+maxtrix[i][j]
print(ans_Ming,dp[-1][-1])
print(dp[-1][-1]+ans_Ming)