class TrieNode:
    def __init__(self):
        # maps characters to children
        self.children = {}
        self.endOfWord = False
class WordDictionary:
    alphabet = "abcdefghijlmnopqrstuvwxyz"
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        agenda = deque([self.root])
        idx = -1 # first node is a dummy

        while agenda:
            idx += 1
            if idx >= len(word):
                return any(node.endOfWord for node in agenda)
            for _ in range(len(agenda)):
                c, node = word[idx], agenda.popleft()
                if c == ".":
                    for child in node.children:
                        agenda.append(node.children[child])
                elif c in node.children:
                    agenda.append(node.children[c])
        return False
        
