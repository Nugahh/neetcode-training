class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif s == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif s == "*":
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif s == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(s))
        return stack[0]

