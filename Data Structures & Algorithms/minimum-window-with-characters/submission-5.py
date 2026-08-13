from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_table = {}
        for char in t:
            t_table[char] = t_table.get(char, 0) + 1

        required = len(t_table)   # distinct chars that must be satisfied
        formed = 0                # how many of them currently ARE satisfied
        cur_table = {}
        idx_stack = deque()       # positions (increasing order) of t-chars in the current window

        best = ""

        for right, char in enumerate(s):
            if char not in t_table:
                continue

            cur_table[char] = cur_table.get(char, 0) + 1
            idx_stack.append(right)
            if cur_table[char] == t_table[char]:
                formed += 1

            while formed == required:
                left = idx_stack[0]          # earliest needed char still in the window
                cur = s[left:right + 1]
                if not best or len(cur) < len(best):
                    best = cur

                idx_stack.popleft()
                left_char = s[left]
                cur_table[left_char] -= 1
                if cur_table[left_char] < t_table[left_char]:
                    formed -= 1

        return best
            

        