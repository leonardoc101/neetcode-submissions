class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": self.add,
            "-": self.sub,
            "/": self.div,
            "*": self.mult,
        }

        stack = []
        for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token[0] == "-" and len(token) != 1:
                stack.append(int(token))
            else:
                new_val = operations[token](stack[-2:])
                stack.pop()
                stack.pop()
                stack.append(new_val)
        return int(stack[0])

    def add(self, stack):
        return sum(stack)

    def sub(self, stack):
        return stack[0] - stack[1]

    def mult(self, stack):
        return stack[0] * stack[1]

    def div(self, stack):
        return int(stack[0] / stack[1])
