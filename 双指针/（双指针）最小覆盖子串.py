'''
https://leetcode-cn.com/problems/minimum-window-substring/
'''
'''
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
示例 1：
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：
输入：s = "a", t = "a"
输出："a"
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        双指针，并用一个数据结构来记录是否满足条件
        '''
        substr = ""
        map_l = {}      #映射check条件map，key:字符，value:数量
        map_l_temp = {}
        for i in t:
            if i not in map_l:
                map_l[i] = 1
            else:
                map_l[i] += 1

        for i in s:
            if i not in map_l_temp:
                map_l_temp[i] = 0

        def check(map_l_temp):
            if len(map_l_temp) < len(map_l):
                return False
            for i in map_l:
                if map_l_temp[i]<map_l[i]:
                    return False
            return True

        def pre_check():
            for i in map_l:
                if i not in map_l_temp:
                    return True
            return False

        left,right = 0,0
        map_l_temp[s[0]] = 1
        flag,flag2 = 0,0
        if pre_check():
            return ""
        while right<len(s):
            if check(map_l_temp):   #如果满足，左指针右移
                if flag and len(s[left:right+1])<len(substr) :
                    substr = s[left:right+1]
                else:
                    flag = 1                    # flag设置在这进行初始化
                    if flag2==0:
                        substr = s[left:right + 1]  # 初始化
                    flag2 = 1
                map_l_temp[s[left]] -= 1
                left += 1
            else:                   #否则，右指针右移
                right += 1
                if right<len(s):
                    map_l_temp[s[right]] += 1
        print(substr)
        return substr



s = "cabwefgewcwaefgcf"
t = "cae"
so = Solution()
so.minWindow(s,t)