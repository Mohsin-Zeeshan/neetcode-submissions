class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # top = stack[-1]

        if (len(s) % 2) == 1:
            return False 


        for i in range(0, len(s)):
            if s[i] == '(' or s[i] ==  '[' or s[i] ==  '{':
                stack.append(s[i])
                
            elif s[i] == ')': 
                if not stack:
                    return False
                top = stack[-1]
                if top == '(':
                    stack.pop()
                else: return False
            elif s[i] == ']': 
                if not stack:
                    return False
                top = stack[-1]
                if top == '[':
                    stack.pop()
                else: return False
            elif s[i] == '}': 
                if not stack:
                    return False
                top = stack[-1]
                if top == '{':
                    stack.pop()
                else: return False
        if not stack:
            return True
        else: 
            return False





    