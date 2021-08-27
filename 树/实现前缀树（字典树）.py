class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None] * 26
        self.end_flag = False

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for index, char in map(lambda x: (ord(x) - ord("a"), x), word):
            # 是否存在,如果不存在，则添加进去
            if root.children[index] is None:
                root.children[index] = Trie()
            root = root.children[index]  # 递归进入
        root.end_flag = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self
        for index, char in map(lambda x: (ord(x) - ord("a"), x), word):
            if root.children[index] is None:
                return False
            root = root.children[index]
        return root.end_flag

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self
        for index, char in map(lambda x: (ord(x) - ord("a"), x), prefix):
            if root.children[index] is None:
                return False
            root = root.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)