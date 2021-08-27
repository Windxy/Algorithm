'''https://leetcode-cn.com/problems/restore-ip-addresses/'''
'''
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：
输入：s = "0000"
输出：["0.0.0.0"]
示例 3：
输入：s = "1111"
输出：["1.1.1.1"]
示例 4：
输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
'''

from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def helper(i,strs,substrs):
            '''
            :param i: 第几层
            :param strs: 剩下的字符串
            :return:
            '''

            nonlocal ans

            if i == 5 and len(strs)==0:      #到达最后一层
                if substrs not in ans:
                    ans.append(substrs)
                return

            if len(strs) > (5-i)*3: # 字符长度过长，剪枝
                return

            if len(strs)==0:
                return

            for index in range(1,4):
                # if i==4 and len(strs)>index:
                #     break
                # if len(strs)<4:
                temp = strs[:index]                     # 用于判断该字符串是否符合
                if int(temp)>255:
                    break
                if len(temp)>1 and temp[0]=='0':        # 开头是0，且大于1的长度
                    break
                if i != 1:                              # 特别判断，用于进行首位不加 '.'
                    helper(i + 1, strs[index:], substrs+'.'+temp)
                else:
                    helper(i + 1, strs[index:], temp)
            return

        helper(1,s,'')
        print(ans)
        return ans

s =Solution()
st = "010010"
s.restoreIpAddresses(st)
