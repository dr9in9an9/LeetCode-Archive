import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone = abs(heapq.heappop_max(stones) - heapq.heappop_max(stones))
            if stone != 0:
                heapq.heappush_max(stones, stone)
        if stones:
            return stones[0]
        return 0
