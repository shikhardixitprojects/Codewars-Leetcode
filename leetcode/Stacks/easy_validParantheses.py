class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if(char == '(' or char == '[' or char == '{'):
                stack.append(char)
            elif(char == ')' and len(stack) > 0 and stack[-1] == '('):
                stack.pop()
            elif(char == ']' and len(stack) > 0 and stack[-1] == '['):
                stack.pop()
            elif(char == '}' and len(stack) > 0 and stack[-1] == '{'):
                stack.pop()
            else:
                return False
        return len(stack) == 0 