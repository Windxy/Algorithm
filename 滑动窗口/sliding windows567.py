
'''
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        dict2 = {}

        # [chr(i) for i in range(97, 123)]
        for i in range(26):
            dict1[chr(i+97)]=0
            dict2[chr(i+97)]=0

        for k in range(len(s1)):
            dict1[s1[k]] += 1

        for i in range(len(s2)):
            if i < len(s1):
                dict2[s2[i]] += 1
                continue

            if dict1 == dict2:
                return True

            else:
                dict2[s2[i]] += 1
                dict2[s2[i-len(s1)]] -= 1
        if dict1 == dict2:
            return True
        return False
s1 = "adc"
s2 = "dcda"
s = Solution()
print(s.checkInclusion(s1,s2))