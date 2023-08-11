class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
                if token == '+': 
                     stack.append(stack.pop() + stack.pop())
                elif token == '/':
                     top_val,lst_val = stack.pop(),stack.pop()
                     stack.append(int(lst_val/ top_val))
                elif token == '-':
                      top_val,lst_val = stack.pop(),stack.pop()
                      stack.append(lst_val - top_val)
                elif token == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    stack.append(int(token))

        return stack[-1]

        #Time and space complexity of O(n)