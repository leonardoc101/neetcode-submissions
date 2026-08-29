class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_hash = Counter(s)
        cur_set = set()
        cur_len = 0
        out = []
        for i in range(len(s)):
            cur_len += 1
            cur_set.add(s[i])
            char_hash[s[i]] -= 1
            if char_hash[s[i]] == 0:
                cur_set.remove(s[i])
                if not cur_set:
                    out.append(cur_len)
                    cur_len = 0
        return out