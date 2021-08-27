from typing import List
def countPairs(deliciousness: List[int]) -> int:
    Dict = {}
    mod = 10 ** 9 + 7
    max_Value = 0
    for i in deliciousness:
        if i > max_Value:
            max_Value = i
        if i not in Dict:
            Dict[i] = 1
        else:
            Dict[i] += 1


    max_Value *= 2

    ans = 0
    for dic in Dict.items():
        x = dic[0]
        z = 1
        while z <= max_Value:
            if z - x < 0:
                pass
            elif z - x in Dict:
                if x == z - x and Dict[x] > 1:  #如果是相同的数字
                    ans += Dict[x] * (Dict[x] - 1)
                elif x!=z-x:                    #如果是不同的数字
                    ans += Dict[x] * Dict[z - x]
            z = z << 1
    print(ans)
    return ans//2 % mod

deli = [1,1,1,3,3,3,7]
countPairs(deli)