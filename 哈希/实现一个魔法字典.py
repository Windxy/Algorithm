# https://leetcode.cn/problems/implement-magic-dictionary/
from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        # 哈希表
        # 映射关系为：单词长度-->【单词1，单词2..】
        self.hashs = defaultdict(list)

    def buildDict(self, dictionary) -> None:
        for di in dictionary:
            self.hashs[len(di)].append(di)

    def search(self, searchWord: str) -> bool:
        if len(searchWord) not in self.hashs:
            return False

        for di in self.hashs[len(searchWord)]:
            flag = 0
            for idx in range(len(di)):
                if di[idx] == searchWord[idx]:
                    continue
                flag += 1
                if flag > 1:    # 超过1个字母不同，换下一个单词试试
                    break
            if flag == 1:
                return True     # 刚好只有一个字母不同
        return False            # 全部单词都不符合