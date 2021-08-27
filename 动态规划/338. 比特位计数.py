from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for x in range(1,num+1):
            temp = ans[x>>1]+(x&1)
            ans.append(temp)
        return ans