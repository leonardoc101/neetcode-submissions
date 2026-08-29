class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = [] # idx
        wildcards = [] # idx

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                elif wildcards:
                    wildcards.pop()
                else:
                    return False
            else:
                wildcards.append(i)
        if not stack:
            return True
        else:
            while stack:
                if not wildcards:
                    return False
                if stack[-1] < wildcards[-1]:
                    stack.pop()
                    wildcards.pop()
                else:
                    return False
            return True
                