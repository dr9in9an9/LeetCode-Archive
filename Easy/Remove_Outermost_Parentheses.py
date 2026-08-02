from collections import deque

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = deque()
        fin = ''
        lef = 0
        rig = 0
        for l in s:
            if l == '(':
                lef += 1
            elif l == ')':
                rig += 1
            if lef != rig:
                stack.append(l)
            else:
                pre = ''
                while len(stack) != 1:
                    pre = stack.pop() + pre
                fin += pre
                stack.pop()
                lef = 0
                rig = 0
        return fin
