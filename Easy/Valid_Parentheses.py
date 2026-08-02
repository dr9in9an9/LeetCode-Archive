class Solution:
    def isValid(self, s: str) -> bool:
        pa = [0,0]
        br = [0,0]
        sq = [0,0]
        stack = deque()
        for l in s:
            match l:
                case '(':
                    pa[0] += 1
                    stack.append(l)
                case ')':
                    pa[1] += 1
                    if pa[1] > pa[0]:
                        return False
                    if stack.pop() != '(':
                        return False
                case '[':
                    br[0] += 1
                    stack.append(l)
                case ']':
                    br[1] += 1
                    if br[1] > br[0]:
                        return False
                    if stack.pop() != '[':
                        return False
                case '{':
                    sq[0] += 1
                    stack.append(l)
                case '}':
                    sq[1] += 1
                    if sq[1] > sq[0]:
                        return False
                    if stack.pop() != '{':
                        return False
        if (len(stack) != 0):
            return False
        return True
