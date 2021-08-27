'''
给一非空的单词列表，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

示例 1：

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/top-k-frequent-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 方法1：计数并排序
        count = Counter(words)
        words = []
        for w,cnt in count.items():
            words.append([w,cnt])
        words.sort(key=lambda x:(-x[1],x[0]))
        return [i[0] for i in words[:k]]





s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(s.topKFrequent(words,k))