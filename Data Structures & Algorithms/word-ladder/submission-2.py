class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0
        
        word_set = set(wordList)
        agenda = deque([beginWord])
        out = 0

        while agenda:
            out += 1
            for _ in range(len(agenda)):
                word = agenda.popleft()
                if word == endWord:
                    return out
                for i in range(len(word)):
                    for c in range(97, 123):
                        if chr(c) == word[i]:
                            continue
                        nei = word[:i] + chr(c) + word[i + 1:]
                        if nei in word_set:
                            word_set.remove(nei)
                            agenda.append(nei)
        return 0