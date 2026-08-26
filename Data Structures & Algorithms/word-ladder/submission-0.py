class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        words, out = set(wordList), 0 
        agenda = deque([beginWord])
        while agenda:
            out += 1
            for _ in range(len(agenda)):
                node = agenda.popleft()
                if node == endWord:
                    return out
                for i in range(len(node)):
                    for c in range(97, 123):
                        if chr(c) == node[i]:
                            continue
                        nei = node[:i] + chr(c) + node [i + 1:]
                        if nei in words:
                            agenda.append(nei)
                            words.remove(nei)
        return 0