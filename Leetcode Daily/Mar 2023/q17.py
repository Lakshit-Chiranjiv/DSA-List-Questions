class Trie:

    def __init__(self):
        self.trie = []
        

    def insert(self, word: str) -> None:
        self.trie.append(word)
        

    def search(self, word: str) -> bool:
        return word in self.trie
        

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for i in self.trie:
            if prefix == i[:n]:
                return True
        return False