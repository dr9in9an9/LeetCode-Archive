class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = [deque(), deque()]
        checking_s = True
        for stack in stacks:
            checking = s
            if checking_s == False:
                checking = t
            for l in checking:
                if l == '#':
                    if len(stack) > 0:
                        stack.pop()
                else:
                    stack.append(l)
            checking_s = False
        
        strings = ['', '']
        i = 0
        for stack in stacks:
            while len(stack) > 0:
                strings[i] += stack.popleft()
            i = 1

        return strings[0] == strings[1]
