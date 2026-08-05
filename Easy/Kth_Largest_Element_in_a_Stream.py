import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify_max(nums)
        self.until_k = []
        self.after_k = nums
        for i in range(0, self.k):
            if len(self.after_k):
                heapq.heappush(self.until_k, heapq.heappop_max(self.after_k))


    def add(self, val: int) -> int:
        heapq.heappush(self.until_k, val)
        if len(self.until_k) > self.k:
            heapq.heappush_max(self.after_k, heapq.heappop(self.until_k))
        return self.until_k[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
