class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == "(":
                stack.append(0)
            
            else:
                val = stack.pop()
                
                if val == 0:
                    stack[-1] += 1
                else:
                    stack[-1] += 2 * val
            
        return stack.pop()
        