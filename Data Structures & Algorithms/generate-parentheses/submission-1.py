class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []

        def backtrack(stack, openN, closedN):
            if openN == closedN == n:
                out.append("".join(stack))
                return
            
            if openN < n:
                backtrack(stack + ["("], openN + 1, closedN)
            if closedN < openN:
                backtrack(stack + [")"], openN, closedN + 1)

        backtrack([], 0, 0)
        return out