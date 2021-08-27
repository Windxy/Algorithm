from typing import List
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        if m==1 or n==1:
            return True
        for i in range(m-1):
            k = i
            d = 0
            while d+1<n and k+1<m:
                if matrix[k][d] != matrix[k+1][d+1]:
                    return False
                k+=1
                d+=1

        for j in range(n):
            k = j
            d = 0
            while d+1<m and k+1<n:
                if matrix[d][k] != matrix[d+1][k+1]:
                    return False
                k+=1
                d+=1
        return True

s = Solution()
mat = [[11,74,0,93],[40,11,74,7]]
ans = s.isToeplitzMatrix(mat)
print(ans)