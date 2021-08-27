# https://leetcode-cn.com/problems/search-a-2d-matrix/
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix),len(matrix[0])
        left,right = 0,m*n-1

        while left<=right:
            mid = (left+right)//2
            temp = matrix[mid//n][mid%n]
            if target == temp:
                return True
            elif target>temp:
                left = mid + 1
            else:
                right = mid - 1
        return False