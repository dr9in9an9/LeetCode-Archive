class RecentCounter:

    def __init__(self):
        self.recent_stack = deque()

    def ping(self, t: int) -> int:
        temp_stack = deque()
        temp_stack.append(t)
        while len(self.recent_stack):
            if t-3000 <= self.recent_stack[-1] <= t:
                temp_stack.append(self.recent_stack.pop())
            else:
                self.recent_stack.clear()
        r = len(temp_stack)
        while len(temp_stack) != 0:
            self.recent_stack.append(temp_stack.pop())
        return r

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
