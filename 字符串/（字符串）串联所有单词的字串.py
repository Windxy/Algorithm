# coding:utf-8
'''
**************************************************
@File   ：python_dp -> （字符串）串联所有单词的字串
@IDE    ：PyCharm
@Author ：Small_wind
@Date   ：2020/9/29 19:20
**************************************************
'''
'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

示例 1：
输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        :param s:  源字符串
        :param words: 字符组合
        :return: List
        '''

        '''暴力法'''
        len_of_words = len(words)
        len_of_s = len(s)
        len_of_word = len(words[0])
        if len_of_s == 0 or len_of_words == 0 or len_of_word == 0:
            return []
        first_digit = [k[0] for k in words]

        ans = []
        '''对于字符串s中的每一个字符组合，都进行遍历查看是否有此'''
        for i in range(len_of_s - len_of_word * len_of_words + 1):
            tmp = words.copy()
            if s[i] not in first_digit:
                continue
            tmp_i = i
            while s[tmp_i:tmp_i+len_of_word] in tmp:
                tmp.remove(s[tmp_i:tmp_i+len_of_word])
                tmp_i += len_of_word

            if len(tmp)==0:
                ans.append(i)
        print(ans)
        return ans

so = Solution()
s = "wordgoodgoodgoodbestword"
words = ["word", "good", "best", "word"]
so.findSubstring(s,words)

