class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] == "*":
                left = stack.pop()
                right = stack.pop()
                a = left * right
                stack.append(a)
            elif tokens[i] == "-":
                left = stack.pop()
                right = stack.pop()
                a = right - left
                stack.append(a)
            elif tokens[i] == "+":
                left = stack.pop()
                right = stack.pop()
                a = left + right
                stack.append(a)
            elif tokens[i] == "/":
                left = stack.pop()
                right = stack.pop()
                a = int(right / left)
                stack.append(a)
            else: stack.append(int(tokens[i]))
        a = stack.pop()
        return a   
