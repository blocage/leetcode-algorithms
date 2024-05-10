class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            curr = curr.children[i]
        
        curr.is_word = True

    def search(self, word: str, is_word=True) -> bool:
        curr = self.root
        for i in word:
            curr = curr.children.get(i)
            if not curr:
                return False
        
        if is_word:
            return curr.is_word
        
        return True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix, False)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)