# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （哈希）查找常用字符
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/10/14 21:22
**************************************************
'''
'''
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
你可以按任意顺序返回答案。
示例 1：
输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：
输入：["cool","lock","cook"]
输出：["c","o"]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        min_length_char = min(A, key=len)
        for char in min_length_char:
            if all(char in item for item in A):
                res.append(char)
                A = [i.replace(char, '', 1) for i in A]

        return res

#
# 作者：JamLeon
# 链接：https: // leetcode - cn.com / problems / find - common - characters / solution / si - lu - jian - dan - xing - neng - jie - jin - shuang - 100 - by - j - 2 /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。