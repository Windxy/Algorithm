#https://leetcode-cn.com/problems/edit-distance/
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''状态转移方程'''
        '''dp[i][j] = dp[i-1][j-1]  if t[i]==j[j]'''
        '''dp[i][j] = min{  
                            dp[i-1][j-1] + 1 , 改
                            dp[i-1][j] + 1 ,   增
                            dp[i][j-1] + 1 ,   增
                        }            if t[i]!=j[j]
        '''
        if len(word1) * len(word2) == 0:
            return len(word1) + len(word2)

            # dp = [[0]*(len(word2)+1)]*(len(word1)+1)          #错误写法
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1)):
            dp[i + 1][0] = i + 1
        for j in range(len(word2)):
            dp[0][j + 1] = j + 1

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[len(word1)][len(word2)]