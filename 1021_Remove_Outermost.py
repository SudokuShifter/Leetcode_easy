class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        checker = 0
        for i in s:
            if i == '(':
                checker += 1
                if checker > 1:
                    stack.append(i)
            else:
                checker -= 1
                if checker > 0:
                    stack.append(i)
        return ''.join(stack)